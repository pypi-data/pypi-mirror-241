"""
This file is part of JuPySub

Author: Pedro de Carvalho Ferreira, Ivo Filot, Ivo Roghair
License: GPLv3
"""

import re
import argparse
from collections import Counter
from jupysub.utils.tags import build_tag
from jupysub.utils.difficulty_bar import difficulty_bar_replacer
from jupysub.utils.NotebookManipulator import NotebookManipulator
from jupysub.utils.documentation_replacer import add_links_to_code
from jupysub.utils.add_expected_outputs import add_expected_outputs

def main():
    """
    The main function for processing Jupyter Notebooks using argparse for command-line options.

    This function utilizes argparse to parse command-line arguments for loading a Jupyter Notebook,
    modifying its contents, and saving the processed notebook. It performs several operations, such as:
    1. Replacing inline code and hints in Markdown cells.
    2. Replacing special blocks in code cells, e.g., ANSWER, EXCLUDE, OPTIONAL.
    3. Running the notebook to update outputs (optional).
    4. Adding links to documentation in Markdown cells.
    5. Adding question numbers <#q>
    6. Adding difficulty emojis
    7. Removing cell outputs.
    8. Saving the processed notebook.

    Command-line Options:
    -i, --infile      : The input notebook file path.
                        Default is './main_notebooks/example.ipynb'.
                        
    -o, --outfile     : The output notebook file path where the processed notebook will be saved.
                        Default is './main_notebooks/example_out.ipynb'.
                        
    -rb, --run-before : Flag. If present, runs the notebook before making any modifications.
    
    -ra, --run-after  : Flag. If present, runs the notebook after all modifications.

    -or, --only-run  : Flag. If present, runs the notebook and saves it under the same name without replacing anything.

    -t, --teacher    : Flag. If present, runs the notebook to make the teacher version, which does not contain expected outputs and example blocks.

    -a, --answer    : Flag. If present, runs the notebook to make the answer version, which does not contain example blocks.

    Inner Functions:
    - optional_replacer(match): Comments out lines inside OPTIONAL blocks.
    - hint_replacer(match)    : Replaces hint text with HTML divs to highlight the hint.

    Example Usage:
    --------------
    $ python -m main -i ./main_notebooks/example.ipynb -o ./main_notebooks/example_out.ipynb -rb
    Runs the file example.ipynb;
    Makes replacements;
    Saves output;

    Returns:
    None

    To parse these command-line options in your script, you can use the following argparse code snippet:
    """
    # Defining the parser for input arguments 
    parser = argparse.ArgumentParser(description="Parser for JuPySub")
    parser.add_argument("-i" , "--infile",     type=str, default=["./main_notebooks/example.ipynb"],     nargs='+', help="input file paths")
    parser.add_argument("-o" , "--outfile",    type=str, default=["./main_notebooks/example_out.ipynb"], nargs='+', help="output file paths")
    parser.add_argument("-rb", "--run-before", default=False, action="store_true", help="run file before substituting patterns")
    parser.add_argument("-ra", "--run-after",  default=False, action="store_true", help="run file after substituting patterns")
    parser.add_argument("-or", "--only-run",  default=False, action="store_true", help="only runs files")
    parser.add_argument("-sc", "--skip-code",  default=False, action="store_true", help="whether to skip code tags")
    parser.add_argument("-t", "--teacher",  default=False, action="store_true", help="doesn't add expected outputs and EXAMPLE blocks")
    parser.add_argument("-a", "--answer",  default=False, action="store_true", help="doesn't add expected outputs and includes EXAMPLE blocks")
    
    # parse the arguments
    args = parser.parse_args()
    
    # Checking that the notebook is student version, teacher version OR answer version
    assert not (args.teacher and args.answer), "Only supposed to use one -a or one -t at a time"

    # Defining some regex
    space = r"[\t ]"
    inline_code  =r"(?<!`)`([^`]+)`(?!`)"
    hint = r"^>\s*\**([a-zA-Z]{1,10}:)\**(.*?)$"
    generic_block = rf"({space}*)#!{space}*BEGIN{space}+BNAME\s*(.*?)\s*#!{space}*END{space}+BNAME({space}*)"
    generic_tag = rf"<tag>content</tag>" # Used to construct html tags
    end_of_script = r"([\n \t]*)\Z" # Used to remove trailing lines
    difficulty_pattern = r"^(#+.*?)<d(\d)/(\d)>" # Used to add difficulty to exercises
    counter_pattern = r"^(#+.*?)<#(\w+)>" # Add a custom counter with code given by a number that increases each time the pattern is found
    answer_block = generic_block.replace("BNAME","ANSWER")
    exclude_block = generic_block.replace("BNAME","EXCLUDE") + r"\n?"
    optional_block = generic_block.replace("BNAME", "OPTIONAL")
    example_block = generic_block.replace("BNAME", "EXAMPLE")

    # Making the replacements

    def optional_replacer(match):
        """ Replaces all lines inside the block by commented lines """
        code = match.group(2)
        space_in_end = match.group(3)
        commented_code = re.sub(rf"^([^\n].*?)$", r"#\1", code, flags=re.MULTILINE|re.DOTALL)
        return commented_code+space_in_end
    
    def hint_replacer(match):
        """ Replaces warnings by html divs of different columns """
        kind = match.group(1).strip(":").lower()
        if kind in ("warning", "careful", "caution"):
            class_ ="danger"
        elif kind in ("note", "detail"):
            class_ ="warning"
        else:
            class_ ="info"
        tag = build_tag("div", {"class":"alert alert-block alert-%s"%class_,
                                 "style":{"border-radius": "6px"}})
        text = "<b>%s</b> %s"%(match.group(1), match.group(2))
        return tag % text
    
    counter = Counter()
    def counter_replacer(match):
        key = match.group(2)
        counter[key] += 1
        return match.group(1) + str(counter[key])
        

    # Adding the replacements to appropriate cell types
    replacements = NotebookManipulator.build_replacement_dict()
    if not args.skip_code:
        replacements["markdown"][inline_code] = generic_tag.replace("tag","code").replace("content", r"\1")
    replacements["markdown"][hint] = hint_replacer

    # Replacing blocks 
    replacements["code"][answer_block] = r"\2" if args.answer else r"\1# ADD YOUR CODE HERE"
    replacements["code"][exclude_block] = r""
    replacements["code"][optional_block] = optional_replacer
    replacements["code"][example_block] = r"\1" if args.teacher else r"\1\2"

    # Replacing empty lines in the end of cells
    replacements["code"][end_of_script] = ""
    replacements["markdown"][end_of_script] = ""

    # Adding question numbers
    replacements["markdown"][counter_pattern] = counter_replacer

    # Adding difficulty
    replacements["markdown"][difficulty_pattern] = difficulty_bar_replacer

    ## Loading the notebook 
    for infile, outfile in zip(args.infile, args.outfile):
        notebook = NotebookManipulator(infile)

        ## If the file only has to be run
        if args.only_run:
            notebook.run_notebook()
            notebook.save(infile)
            continue 

        ## Notebook processing
        # Runing the notebook to renew the outputs 
        if args.run_before:
            notebook.run_notebook() 

        # Adding expected output blocks
        if not (args.teacher or args.answer):
            add_expected_outputs(notebook)

        # Replacing markdown and code 
        notebook.apply_replacements(replacements)

        # Adding links to documentation (after the code was enclosed in <code></code> blocks)
        url_replacements = NotebookManipulator.build_replacement_dict()
        url_replacements["markdown"][r'(<code.*?>)(.*?)(</code>)'] = add_links_to_code
        notebook.apply_replacements(url_replacements)

        # removing cell outputs 
        notebook.remove_cell_outputs()

        # Runing after if instructed 
        if args.run_after:
            notebook.run_notebook()

        ## Saving the final result 
        notebook.save(outfile)

if __name__ == "__main__":
    main()
