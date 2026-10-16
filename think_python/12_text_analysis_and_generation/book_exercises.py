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


def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve

        local, _ = urlretrieve(url, filename)
        print("Downloaded " + str(local))
    return filename


# The following cell downloads the book from Project Gutenberg.
download('https://www.gutenberg.org/cache/epub/43/pg43.txt');

# The version available from Project Gutenberg includes information about the book
# at the beginning and license information at the end.
# We'll use `clean_file` from Chapter 8 to remove this material
# and write a "clean" file that contains only the text of the book.


def is_special_line(line):
    return line.strip().startswith('*** ')


def clean_file(input_file, output_file):
    reader = open(input_file)
    writer = open(output_file, 'w')

    for line in reader:
        if is_special_line(line):
            break

    for line in reader:
        if is_special_line(line):
            break
        writer.write(line)

    reader.close()
    writer.close()


filename = 'dr_jekyll.txt'

clean_file('pg43.txt', filename)

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

