# 8.12. Exercises

# 8.12.1. Ask a virtual assistant
# In this chapter, we only scratched the surface of what regular expressions can do.
# To get an idea of what’s possible, ask a virtual assistant,
# “What are the most common special characters used in Python regular expressions?”

# Most common regex special characters (Python re module):
# .      matches any single character except newline
# ^      matches start of string
# $      matches end of string
# *      zero or more repetitions of preceding element
# +      one or more repetitions of preceding element
# ?      zero or one repetition / enable non‑greedy mode
# []     character set definition
# ()     capture grouping
# |      alternation (OR)
# \      escape metacharacters or special sequences like \d \w \s
# Tip: use raw string r"" for regex patterns to avoid backslash issues


# You can also ask for a pattern that matches particular kinds of strings. For example, try asking:
# Write a Python regular expression that matches a 10-digit phone number with hyphens.
import re

# pattern: 3digits - 3digits -4digits
pattern = r"\d{3}-\d{3}-\d{4}"

# test
print('\nmatches  a 10-digit phone number with hyphens')
text1 = "123-456-7890"
text2 = "1234567890"
print(re.fullmatch(pattern, text1))  # match
print(re.fullmatch(pattern, text2))  # no match

# Write a Python regular expression that matches a street address with a number and a street name, followed by ST or AVE.

# Pattern: house number + street name + ends with ST or AVE
# Example matches: "123 Main ST", "45 Oak AVE"
pattern = r"\d+ [A-Za-z]+ (ST|AVE)$"


def match_address(address_text):
    return re.fullmatch(pattern, address_text) is not None


# test cases
print('\nmatches a street address with a number and a street name')
print(match_address("123 Main ST"))   # True
print(match_address("45 Oak AVE"))     # True
print(match_address("789 Pine ROAD"))  # False, ends with ROAD
print(match_address("Main ST"))        # False, no house number

# Write a Python regular expression that matches a full name with any common title
# like Mr or Mrs followed by any number of names beginning with capital letters, possibly with hyphens between some names.

# Matches full name with title Mr or Mrs
# Examples: "Mr John Smith", "Mrs Mary Ann‑Jones", "Mr Anna‑Lee Clark"
pattern = r"^(Mr|Mrs)( [A-Z][A-Za-z\-]+)+$"
# **Regex breakdown:**

# - `^` start of string
# - `(Mr|Mrs)` match title Mr or Mrs
# - ` ` literal space after title
# - `[A-Z]` each name segment **starts with capital letter**
# - `[A-Za-z\-]+` rest of segment: letters or hyphen
# - `+` one or more name segments (can have multiple given / last names)[One or more repetitions of preceding pattern]
# - `$` end of string


def check_name(name_str):
    return re.fullmatch(pattern, name_str) is not None


# test cases
print('\nMatches full name with title Mr or Mrs')
print(check_name("Mr John Smith"))        # True
print(check_name("Mrs Mary Ann‑Jones"))    # True
print(check_name("Mr anna‑Lee Clark"))     # False: anna starts lowercase
print(check_name("Mr  john Smith"))         # False: extra space
print(check_name("Ms Jane Doe"))            # False: Ms not allowed

# And if you want to see something more complicated, try asking for a regular expression that matches any legal URL.

# Simplified URL regex (http / https scheme)
url_pattern = r"https?://[^\s]+"

# `https?://` : `http://` or `https://`; `?` makes `s` optional
# ^ Start of string / start of line
# \s whitespace (space, tab, newline)
# + One or more repetitions of preceding pattern
# `[^\s]+` : one or more characters **except whitespace** (stop at first space)


def is_url(text):
    return re.fullmatch(url_pattern, text) is not None


# Test
print('\nmaches any legal url')
print(is_url("https://www.google.com"))  # True
print(is_url("http://my‑site.org/page?id=123"))  # True
print(is_url("not a url"))  # False

# 8.12.2. Exercise

# See if you can write a function that does the same thing as the shell command !head.
# It should take as arguments the name of a file to read,
# the number of lines to read,
# and the name of the file to write the lines into.
# If the third parameter is None, it should display the lines rather than write them to a file.

# Consider asking a virtual assistant for help, but if you do, tell it not to use a with statement or a try statement.


def head(file_in_name, num_lines, file_out_name):
    reader = open(file_in_name)
    count = 0
    if file_out_name is not None:
        writer = open(file_out_name, 'w')
    while count < num_lines:
        line = reader.readline()
        # empty string means reached end‑of‑file
        if not line:
            break
        if file_out_name is None:
            print(line, end="")
        else:
            writer.write(line)
        count = count + 1
    reader.close()
    if file_out_name is not None:
        writer.close()


# 8.12.3. Exercise

# “Wordle” is an online word game where the objective is to guess a five-letter word in six or fewer attempts.
# Each attempt has to be recognized as a word, not including proper nouns.
# After each attempt, you get information about which of the letters you guessed appear in the target word,
# and which ones are in the correct position.

"""
For example, suppose the target word is MOWER and you guess TRIED. 
You would learn that E is in the word and in the correct position,
 R is in the word but not in the correct position, and T, I, and D are not in the word.
 
 As a different example, suppose you have guessed the words SPADE and CLERK, and you’ve learned that E is in the word,
  but not in either of those positions, and none of the other letters appear in the word.
   Of the words in the word list, how many could be the target word?
"""

# Write a function called check_word that takes a five-letter word and
# checks whether it could be the target word, given these guesses.

# You can use any of the functions from the previous chapter, like uses_any.


def uses_any(word, letters):
    for letter in word:
        if letter in letters:
            return True
    return False


def check_word(word):
    word = word.lower()

    # The target word must contain E.
    if 'e' not in word:
        return False

    # E cannot be in the 3rd or 5th position.
    if word[2] == 'e' or word[4] == 'e':
        return False

    # These letters do not appear in the target word.
    forbidden = 'spadclrk'
    if uses_any(word, forbidden):
        return False

    return True


# count = 0
#
# with open('words.txt') as file:
#     for line in file:
#         word = line.strip()
#
#         if len(word) == 5 and check_word(word):
#             count += 1
#
# print(count)


# 8.12.4. Exercise
# Continuing the previous exercise, suppose you guess the work TOTEM and learn that
# the E is still not in the right place, but the M is. How many words are left?


def check_word(word):
    word = word.lower()

    if len(word) != 5:
        return False

    if 'e' not in word:
        return False

    if word[2] == 'e' or word[3] == 'e' or word[4] == 'e':
        return False

    if word[4] != 'm':
        return False

    forbidden = 'spadclrk'
    if uses_any(word, forbidden):
        return False

    return True


count = 0

with open('words.txt') as file:
    for line in file:
        word = line.strip()

        if check_word(word):
            count += 1

print(count)

# 8.12.5. Exercise

# count the number of lines that contain the word pale in any form, including pale, pales, paled, and paleness,
# as well as the related word pallor. Use a single regular expression that matches any of these words.
pattern = r'pale(s|d|ness)?|pallor'
# ? matches the precede once or zero time

# As an additional challenge, make sure that it doesn’t match any other words,
# like impale – you might want to ask a virtual assistant for help.
pattern = r'\b(pale(s|d|ness)?|pallor)\b'  # \b is word boundary
