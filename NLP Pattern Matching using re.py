import re

my_string = 'Let\'s write RegEx!  Won\'t that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?'
#sentence_ending = r'[.,!,?]'
print(re.split('r[.!?]',my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words,my_string))

spaces = r"\s+"
print(re.split(spaces,my_string))

digits = r"\d+"
print(re.findall(digits,my_string))