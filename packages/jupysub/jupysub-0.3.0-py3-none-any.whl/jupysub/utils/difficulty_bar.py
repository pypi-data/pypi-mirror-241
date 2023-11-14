"""
This file is part of JuPySub

Author: Pedro de Carvalho Ferreira, Ivo Filot, Ivo Roghair
License: GPLv3
"""
import re 

# Dictionary of emojis with their UTF-8 codes
emoji_utf8_dict = {
    'Fire': ('🔥', b'\xF0\x9F\x94\xA5'),
    'Star': ('★', b'\xE2\x98\x85'),
    'Heart': ('❤️', b'\xE2\x9D\xA4\xEF\xB8\x8F'),
    'Chili': ('🌶️', b'\xF0\x9F\x8C\xB6'),
    "Brain": ('🧠', b'\xf0\x9f\xa7\xa0')
}

def create_difficulty_html(difficulty, maximum_difficulty, emoji_char, 
                           font_size="10pt", opacity_diff=1, opacity_max_diff=0.1):
    # Create the full-opacity emojis
    full_opacity_block = emoji_char * difficulty
    
    # Create the less opaque emojis
    less_opacity_block = emoji_char * (maximum_difficulty - difficulty)
    
    # Combine into one HTML block
    html_block = f"""
    <span style="font-size: %s;">
        <span style="opacity: {opacity_diff};">{full_opacity_block}</span>
        <span style="opacity: {opacity_max_diff};">{less_opacity_block}</span>
    </span>"""%font_size
    
    return html_block


def difficulty_bar_replacer(match):
    emoji = emoji_utf8_dict["Brain"][0]
    dif, max_diff = tuple(map(int, [match.group(2), match.group(3)]))
    emoji_html = create_difficulty_html(dif, max_diff, emoji)
    return match.group(1) + re.sub(r"(?<=>)\s+(?=<)|^\s+|\t+|\n+","", emoji_html)

# Example usage
if __name__ == "__main__":
    difficulty = 3
    maximum_difficulty = 5
    emoji_char, utf8_code = emoji_utf8_dict['Fire']

    html_result = create_difficulty_html(difficulty, maximum_difficulty, emoji_char)
    print(f"HTML block for difficulty representation:\n{html_result}")
