# Jupyter Notebook Processing Script Documentation

- [Jupyter Notebook Processing Script Documentation](#jupyter-notebook-processing-script-documentation)
  - [Overview](#overview)
- [Getting Started](#getting-started)
  - [Command-Line Interface](#command-line-interface)
    - [Command-line Options](#command-line-options)
    - [Example Usage](#example-usage)
      - [Example of markdown cell before and after replacements:](#example-of-markdown-cell-before-and-after-replacements)
  - [Handling Expected Output](#handling-expected-output)
    - [Expected Output in Markdown Cells](#expected-output-in-markdown-cells)
  - [Auto-linking Functions with Inline Code in Markdown Cells](#auto-linking-functions-with-inline-code-in-markdown-cells)
    - [How to Use](#how-to-use)
    - [Example Usage](#example-usage-1)
  - [Detailed Replacements](#detailed-replacements)
    - [Markdown Cells](#markdown-cells)
      - [Inline Code Replacement](#inline-code-replacement)
      - [Hint Replacement](#hint-replacement)
      - [Exercise Number Replacement](#exercise-number-replacement)
      - [Exercise Difficulty Replacement](#exercise-difficulty-replacement)
    - [Code Cells](#code-cells)
      - [Answer Blocks](#answer-blocks)
      - [Exclude Blocks](#exclude-blocks)
      - [Optional Blocks](#optional-blocks)
  - [Inline Code Replacement](#inline-code-replacement-1)
    - [Example](#example)
      - [Before:](#before)
      - [After:](#after)
    - [Hint Replacement (Colored divs)](#hint-replacement-colored-divs)
      - [End-of-Script Cleanup](#end-of-script-cleanup)
  - [Customization](#customization)

## Overview
This documentation serves as a comprehensive guide for the Jupyter Notebook Processing Script, a Python utility designed to automate various modifications and enhancements on Jupyter Notebooks. Whether you're a student, instructor, or data scientist, this script helps streamline your Jupyter Notebook workflow by handling repetitive tasks such as formatting and running cells, as well as adding useful features like auto-linking to documentation and displaying expected outputs.

The script utilizes Python's `argparse` library for command-line interface, allowing you to specify options such as input and output files, and whether to run the notebook before or after modifications.

Here's what the script can do for you:

- **Run Notebook**: Before or after making modifications, as specified.
- **Formatting**: Automatic conversion of inline code and hints in Markdown cells.
- **Expected Output**: Captures and displays the expected output of code cells.
- **Auto-linking**: Adds hyperlinks to known functions in Markdown cells.
- **Customizable**: Highly configurable through regular expressions and replacement functions.

For detailed usage and customization options, please refer to the sections below.

# Getting Started

## Command-Line Interface

The script leverages Python's `argparse` library to provide a command-line interface. Below are the options that you can specify:

### Command-line Options

| Option              | Description                                                  | Default Value                          |
|---------------------|--------------------------------------------------------------|----------------------------------------|
| `-i, --infile`      | Specifies the path to the input notebook file.               | `./main_notebooks/example.ipynb`       |
| `-o, --outfile`     | Specifies the path to the output notebook file.              | `./main_notebooks/example_out.ipynb`   |
| `-rb, --run-before` | Runs the notebook before making any modifications.           | Not set                                |
| `-ra, --run-after`  | Runs the notebook after all modifications are made.          | Not set                                |
| `-sc, --skip-code`  | Skip replacement of backticks for `<code>`` tags             | Not set                                |

### Example Usage

To illustrate how to use these command-line options, consider the following example:

```bash
$ jupysub -i ./main_notebooks/example.ipynb -o ./main_notebooks/example_out.ipynb -rb -ra
```

1. Runs the file `./main_notebooks/example.ipynb`
2. Performs several substitutions (see more below)
3. Adds an html box under each code cell with the expected cell output
4. Adds url's to documentations of known functions to markdown
5. Adds difficulty rating to the exercises
6. Adds question number <#q>
7. Runs the file a second time
8. Saves the result under `./main_notebooks/example_out.ipynb` 

#### Example of markdown cell before and after replacements:
Before:
```markdown
# Sample Jupyter Notebook Markdown Cell

In this notebook, we are going to explore data transformation using Python. You can use `pandas` to clean the data and `matplotlib` to plot graphs.

> **Note:** Make sure to install all dependencies before running the notebook.

> **Warning:** Be careful when manipulating data. Always double-check your code.

Here is a Python code cell that includes blocks that will be transformed:

-------------------------
#!BEGIN ANSWER
x = 10
y = 20
#!END ANSWER

#!BEGIN EXCLUDE
print("This line will be excluded.")
#!END EXCLUDE

#!BEGIN OPTIONAL
print("This line will be commented out.")
#!END OPTIONAL
-------------------------
```

After:
```markdown
# Sample Jupyter Notebook Markdown Cell

In this notebook, we are going to explore data transformation using Python. You can use <code>pandas</code> to clean the data and <code>matplotlib</code> to plot graphs.

<div class="alert alert-block alert-warning" style="border-radius: 6px">
<b>Note:</b> Make sure to install all dependencies before running the notebook.
</div>

<div class="alert alert-block alert-danger" style="border-radius: 6px">
<b>Warning:</b> Be careful when manipulating data. Always double-check your code.
</div>

Here is a Python code cell that includes blocks that will be transformed:


-------------------------
# ADD YOUR CODE HERE

# print("This line will be commented out.")
-------------------------

Expected output:

-------------------------

This line will be excluded.
This line will be commented out.

-------------------------
```

## Handling Expected Output

### Expected Output in Markdown Cells

- **Methodology**: The script captures the actual output of each code cell upon execution. This can include text or images.
- **Description**: Places the captured output in a new Markdown cell below the corresponding code cell. The output is enclosed within a toggleable HTML `div`, allowing users to choose whether or not they wish to see the expected output.

  **Example**:

    - **Before**:  
      A Python cell that prints "Hello, World!"

      ```python
      print("Hello, World!")
      ```

    - **After**:  
      The original Python cell followed by a new Markdown cell with the captured output and toggle feature.

      ```python
      print("Hello, World!")
      ```

      
      <details>
      <summary>Click to toggle expected output</summary>
      Hello, World!
      
      </details>
      


## Auto-linking Functions with Inline Code in Markdown Cells

The `NotebookManipulator` class allows you to automatically add hyperlinks to functions from libraries like NumPy, Pandas, Matplotlib, SciPy, and the Python Standard Library in markdown cells. This is facilitated through the `apply_replacements` method and a special function `add_links_to_code`.

### How to Use

1. **Build the Replacement Dictionary**: First, initialize the replacement dictionary by calling `NotebookManipulator.build_replacement_dict()`.

    ```python
    replacements = NotebookManipulator.build_replacement_dict()
    ```

2. **Configure Inline Code Replacements**: Add a regular expression pattern for inline code to the "markdown" section of the replacement dictionary. Use the `add_links_to_code` function for replacements.

    ```python
    replacements["markdown"][r'(<code.*?>)(.*?)(</code>)'] = add_links_to_code
    ```

3. **Apply the Replacements**: Finally, apply these replacements to the notebook.

    ```python
    notebook.apply_replacements(replacements)
    ```

### Example Usage

Here's how you could use these steps in a complete example:

```python
# Initialize NotebookManipulator and the replacement dictionary
note = NotebookManipulator("your_notebook.ipynb")
replacements = NotebookManipulator.build_replacement_dict()

# Configure URL replacements for inline code
replacements["markdown"][r'(<code.*?>)(.*?)(</code>)'] = add_links_to_code

# Apply the replacements
note.apply_replacements(replacements)

# Save the notebook
note.save("your_modified_notebook.ipynb")
```

So `np.loadtxt()` for example would be enclosed in a relatively long html tag that would give link the user to the documentation.


## Detailed Replacements

### Markdown Cells

#### Inline Code Replacement

- **Regular Expression Used**: `inline_code  =r"(?<!`)`([^`]+)`(?!`)"`

- **Description**: Finds inline code snippets encapsulated in backticks and replaces them with HTML `<code>` tags.

- **Example**:

  - **Before**: ``` `print()` ```
  - **After**: `<code>print()</code>`

#### Hint Replacement

- **Regular Expression Used**: `hint = r"^>\s*\**([a-zA-Z]{1,10}:)\**(.*?)$"`

- **Description**: Transforms Markdown-styled hints into styled HTML `div` blocks.

- **Example**:

  - **Before**: `> **Note:** This is a note.`
  - **After**: `<div class="alert alert-block alert-warning"><b>Note:</b> This is a note.</div>`


#### Exercise Number Replacement

- **Regular Expression Used**: Uses the pattern `r"^(#.*?)<#(\w+)>"` to find sections marked for exercise numbering.

- **Description**: Looks for exercise headers containing `<#key>` and replaces it with an incrementing counter based on the key specified. This is useful for automatic numbering of exercises in a document.

- **Example**:

  - **Before**:
    ```markdown
    ## Exercise <#q>: Helo
    ## Exercise <#q>: Heloo
    ```
  - **After**:
    ```markdown
    ## Exercise 1: Helo
    ## Exercise 2: Heloo
    ```


#### Exercise Difficulty Replacement

- **Regular Expression Used**: Uses the pattern `r"^(#.*?)<d(\d)/(\d)>"` to find sections marked for difficulty rating.

- **Description**: Replaces `<dX/Y>` with a visual rating system using emojis. `X` is the number of filled emojis to show, and `Y` is the total number of emojis. Emojis with reduced opacity represent the remaining difficulty points.

- **Example**:

  - **Before**:
    ```markdown
    ## Question <#q>: Heat transfer <d3/5>
    ## Question <#q>: Another Heat transfer <d2/5>
    ```
  - **After**:
    ```markdown
    ## Question 1: Heat transfer <span style="font-size: 10pt;"><span style="opacity: 1;">🧠🧠🧠</span><span style="opacity: 0.1;">🧠🧠</span></span>
    ## Question 2: Another Heat transfer <span style="font-size: 10pt;"><span style="opacity: 1;">🧠🧠</span><span style="opacity: 0.1;">🧠🧠🧠</span></span>
    ```

### Code Cells

#### Answer Blocks

- **Regular Expression Used**: Uses a generic pattern to find blocks tagged `ANSWER`.

- **Description**: Replaces the entire code block tagged with `ANSWER` with a placeholder for students or users to fill in.

- **Example**:

  - **Before**:
    ```python
    #!BEGIN ANSWER
    x = 10
    y = 20
    #!END ANSWER
    ```
  - **After**:
    ```python
    # ADD YOUR CODE HERE
    ```

#### Exclude Blocks

- **Regular Expression Used**: Uses a generic pattern to find blocks tagged `EXCLUDE`.

- **Description**: Deletes the entire code block tagged with `EXCLUDE`.

- **Example**:

  - **Before**:
    ```python
    #!BEGIN EXCLUDE
    print("This should be excluded.")
    #!END EXCLUDE
    ```
  - **After**: 
    ```python
    ```

#### Optional Blocks

- **Regular Expression Used**: Uses a generic pattern to find blocks tagged `OPTIONAL`.

- **Description**: Comments out the code inside blocks tagged `OPTIONAL`.

- **Example**:

  - **Before**:
    ```python
    #!BEGIN OPTIONAL
    print("This is optional.")
    #!END OPTIONAL
    ```
  - **After**: 
    ```python
    # print("This is optional.")
    ```

## Inline Code Replacement

This operation targets inline code elements in Markdown cells. The aim is to ensure that the inline code renders correctly when the notebook is converted to HTML or other formats.

### Example

#### Before:

    Here, we are talking about `x` and `y`.

#### After:

    Here, we are talking about `<code>x</code>` and `<code>y</code>`.

---

### Hint Replacement (Colored divs)

- **Regular Expression Used**: `hint = r"^>\s*\**([a-zA-Z]{1,10}:)\**(.*?)$"`
  
- **Description**: Transforms Markdown-styled hints into styled HTML `div` blocks. The `div` class changes based on the type of hint, meaning the hint box will be colored differently for different types of hints.
  
  **Examples**:
    
    - **Type: Warning**
        - **Before**: `> **Warning:** Be careful with this step.`
        - **After**: 
        ```html
        <div class="alert alert-block alert-danger" style="border-radius: 6px">
        <b>Warning:</b> Be careful with this step.
        </div>
        ```
        
    - **Type: Note**
        - **Before**: `> **Note:** This is an important point.`
        - **After**: 
        ```html
        <div class="alert alert-block alert-warning" style="border-radius: 6px">
        <b>Note:</b> This is an important point.
        </div>
        ```
    
    - **Type: Info**
        - **Before**: `> **Info:** Additional details here.`
        - **After**: 
        ```html
        <div class="alert alert-block alert-info" style="border-radius: 6px">
        <b>Info:</b> Additional details here.
        </div>
        ```


#### End-of-Script Cleanup

- **Regular Expression Used**: `end_of_script = r"([\n \t]*)\Z"`

- **Description**: Removes trailing white spaces and new lines at the end of each cell.

- **Example**:

  - **Before**: 
    ```python
    print("Hello World")
    
    ```
  - **After**:
    ```python
    print("Hello World")
    ```

## Customization

The script is designed to be highly customizable. Feel free to change the regular expressions, the replacement functions, or even the order of the operations to suit your specific needs.
