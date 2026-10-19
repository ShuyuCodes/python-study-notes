from os.path import basename, exists

# 12. Text Analysis and Generation

# we have covered Python’s core data structures – lists, dictionaries, and tuples –
# and some algorithms that use them. In this chapter, we’ll use them to explore text analysis and Markov generation:
#
# Text analysis is a way to describe the statistical relationships between the words in a document,
# like the probability that one word is followed by another, and

#  Markov generation is a way to generate new text with words and phrases similar to the original text.

# 12.1. Unique words

# As a first step toward text analysis, let's read a book -- *The Strange Case Of Dr. Jekyll And Mr. Hyde*
# by Robert Louis Stevenson -- and count the number of unique words.


# def download(url):
#     filename = basename(url)
#     if not exists(filename):
#         from urllib.request import urlretrieve
#
#         local, _ = urlretrieve(url, filename)
#         print("Downloaded " + str(local))
#     return filename
#
#
# # The following cell downloads the book from Project Gutenberg.
# download('https://www.gutenberg.org/cache/epub/43/pg43.txt');
#
# # The version available from Project Gutenberg includes information about the book
# # at the beginning and license information at the end.
# # We'll use `clean_file` from Chapter 8 to remove this material
# # and write a "clean" file that contains only the text of the book.
#
#
# def is_special_line(line):
#     return line.strip().startswith('*** ')
#
#
# def clean_file(input_file, output_file):
#     reader = open(input_file)
#     writer = open(output_file, 'w')
#
#     for line in reader:
#         if is_special_line(line):
#             break
#
#     for line in reader:
#         if is_special_line(line):
#             break
#         writer.write(line)
#
#     reader.close()
#     writer.close()


# file has been created
filename = 'dr_jekyll.txt'

# clean_file('pg43.txt', filename)

unique_words = {}

with open(filename) as reader:
    for line in reader:
        seq = line.split()
        for word in seq:
            unique_words[word] = 1  # If word is already a key in the dictionary,
            # Python updates its existing value to 1. It does not create a duplicate key.

print(len(unique_words))

print(sorted(unique_words, key=len)[-5:])

# 12.2. Punctuation


def split_line(line):  # replace DASH with a space, then use split to remove punctuation
    return line.replace('—', ' ').split()


print(split_line('from 3 - 5,'))  # it leaves hyphenated words alone.

print(split_line('coolness—frightened'))

# Characters in Python strings are in Unicode, which is an international standard used to represent letters
# in nearly every alphabet, numbers, symbols, punctuation marks, and more. The unicodedata module provides
# a category function we can use to tell which characters are punctuation.

import unicodedata

print(unicodedata.category('A'))  # Lu - L letter, u uppercase

print(unicodedata.category('a'))  # Ll

print(unicodedata.category('.'))  # Po - P punctuation, o other subcategory

# We can find the punctuation marks in the book by checking for characters with categories that begin with 'P'.
# The following loop stores the unique punctuation marks in a dictionary.

punc_marks = {}
with open (filename, encoding='utf-8') as reader:
    for line in reader:
        for char in line:
            category = unicodedata.category(char)
            if category.startswith('P'):
                punc_marks[char] = 1

# To make a list of punctuation marks, we can join the keys of the dictionary into a string.
punctuation = ''.join(punc_marks)
print(punctuation)

# Now that we know which characters in the book are punctuation, we can write a function that takes a word,
# strips punctuation from the beginning and end, and converts it to lower case.


def clean_word(word):  # takes a word, strips punctuation from the beginning and end, and converts it to lower case.
    return word.strip(punctuation).lower()

# print(clean_word('“Behold!”'))  # behold
print(clean_word('pocket-handkerchief'))  # it leaves hyphenated word alone

# Now here’s a loop that uses split_line and clean_word to identify the unique words in the book.
unique_words2 = {}
with open (filename, encoding='utf-8') as reader:
    for line in reader:
        for word in split_line(line):
            word = clean_word(word)
            unique_words2[word] = 1

print(len(unique_words2))

# there are about 4000 unique words. And we can confirm that the list of longest words has been cleaned up.

print(sorted(unique_words2, key=len)[-5:])

# Now let’s see how many times each word is used.

# 12.3. Word frequencies

# The following loop computes the frequency of each unique word.
word_counter = {}
with open (filename, encoding='utf-8') as reader:
    for line in reader:
        for word in split_line(line):
            word = clean_word(word)
            if word not in word_counter:  # The first time we see a word, we initialize its frequency to 1. If we see the same word again later, we increment its frequency.
                word_counter[word] = 1
            else:
                word_counter[word] += 1


def second_element(t):  # select the second element
    return t[1]


items = sorted(word_counter.items(), key=second_element, reverse=True)
# key=second_element means the items will be sorted according to the frequencies of the words.
# reverse=True means the items will be sorted in reverse order, with the most frequent words first.

# Here are the five most frequent words.
# for word, freq in items[:5]:
#     print(freq, word, sep='\t')  # separated by a tab

# an f-string with a fixed-width field, this looks more neat
for word, freq in items[:5]:
    print(f'{freq:<6}{word}')
# < aligns the frequency to the left.
# 6 reserves six character positions for the frequency.
# word follows immediately after that field.

# In the next section, we’ll encapsulate this loop in a function. And we’ll use it to demonstrate a new feature – optional parameters.

# 12.4. Optional parameters

#  ndigits  indicates how many decimal places to keep.
print(round(3.141592653589793, ndigits=3))

# But it’s not just built-in functions – we can write functions with optional parameters, too.
# For example, the following function takes two parameters, word_counter and num.


def print_most_common(word_counter, num=5):  # The second parameter looks like an assignment statement,
    # but it’s not – it’s an optional parameter.
    """Print the most common words in word_counter sorted by frequency."""
    items = sorted(word_counter.items(), key=second_element, reverse=True)

    for word, freq in items[:num]:
        print(f'{freq:<6}{word}')


print_most_common(word_counter)  # call this function with one argument, num gets the default value, which is 5.

print_most_common(word_counter, 3)  # call this function with two arguments, the second argument gets assigned to num instead of the default value.
# In that case, we would say the optional argument overrides the default value.

# if a function has both required and optional parameters, all of the required parameters have to come first, followed by the optional ones.

# 12.5. Dictionary subtraction

# Suppose we want to spell-check a book – that is, find a list of words that might be misspelled.
# One way to do that is to find words in the book that don’t appear in a list of valid words.

# In previous chapters, we’ve used a list of words that are considered valid in word games like Scrabble.

# we can read the contents of words.txt and split it into a list of strings.
with open ('../words.txt') as reader:
    word_list = reader.read().split()

valid_words = {}
for word in word_list:
    valid_words[word] = 1

# Now, to identify words that appear in the book but not in the word list, we’ll use subtract,
# which takes two dictionaries as parameters and returns a new dictionary
# that contains all the keys from one that are not in the other.


def subtract(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = d1[key]
    return res


diff = subtract(word_counter, valid_words)

print()
print_most_common(diff)
# The most common “misspelled” words are mostly names and a few single-letter words (Mr. Utterson is Dr. Jekyll’s friend and lawyer).

# If we select words that only appear once, they are more likely to be actual misspellings.
# We can do that by looping through the items and making a list of words with frequency 1.
singletons = []
for word, freq in diff.items():
    if freq == 1:
        singletons.append(word)

print(singletons[-5:])  # In Python, dictionaries preserve insertion order in Python 3.7 and later.
print(singletons[: 5])

# 12.6. Random numbers

# As a step toward Markov text generation, next we’ll choose a random sequence of words from word_counter.
# But first let’s talk about randomness.

# Given the same inputs, most computer programs are deterministic, which means they generate the same outputs every time.
# Making a program truly nondeterministic turns out to be difficult, but there are ways to fake it.
# One is to use algorithms that generate pseudorandom numbers

# Pseudorandom numbers are not truly random because they are generated by a deterministic computation,
# but just by looking at the numbers it is all but impossible to distinguish them from random.

# The random module provides functions that generate pseudorandom numbers –
# which I will simply call “random” from here on. We can import it like this.

import random

# The random module provides a function called choice that chooses an element from a list at random,
# with every element having the same probability of being chosen
t = [1, 2, 3]
print(random.choice(t))

# If you use choice with a dictionary, you get a KeyError.
# random.choice(word_counter)

# To choose a random key, you have to put the keys in a list and then call choice.
words = list(word_counter)
print(random.choice(words))

# next sections are in b_exercises.ipynb file
