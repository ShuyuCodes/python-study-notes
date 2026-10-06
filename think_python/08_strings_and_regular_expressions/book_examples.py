# 8. Strings and Regular Expressions

# Strings are not like integers, floats, and booleans.
# A string is a sequence, which means it contains multiple values in a particular order.

# regular expressions, which are a powerful tool for finding patterns in a string and performing operations
# like search and replace

# 8.1. A string is a sequence
fruit = 'banana'
letter = fruit[1]
print(letter)

# 8.2. String slices
print(fruit[0:3])
print(fruit[:3])
print(fruit[3:])

print(fruit[3:3])  # If the first index is greater than or equal to the second, the result is an empty string

# 8.3. Strings are immutable
greeting = 'Hello, world!'
# greeting[0] = 'J'  # TypeError: 'str' object does not support item assignment

new_greeting = 'Hej' + greeting[5:]
print(new_greeting)

print(greeting)

# 8.4. String comparison

word = 'banana'

if word == 'banana':
    print('All right, banana.')


def compare_word(word):
    if word < 'banana':
        print(word, 'comes before banana.')
    elif word > 'banana':
        print(word, 'comes after banana.')
    else:
        print('All right, banana.')


compare_word('apple')

# All the uppercase letters come before all the lowercase letters

compare_word('Pineapple')

# 8.5. String methods

# Instead of the function syntax upper(word), it uses the method syntax word.upper().
word = 'banana'

# A method call is called an invocation; in this case, we would say that we are invoking upper on word.
new_word = word.upper()

print(new_word)

# 8.6. Writing files

# there is a downloaded the book in a plain text file called pg345.txt, but there is noly a fake file with the same name

reader = open('pg345.txt')

# the startswith method, which checks whether a string starts with a given sequence of characters.


def is_special_line(line):
    return line.startswith('*** ')


for line in reader:
    if is_special_line(line):
        print(line.strip())

# *** START OF THE PROJECT GUTENBERG EBOOK DRACULA ***
# *** END OF THE PROJECT GUTENBERG EBOOK DRACULA ***

reader.close()

# Now let’s create a new file, called pg345_cleaned.txt, that contains only the text of the book.
# In order to loop through the book again, we have to open it again for reading.

# to write a new file, we can open it for writing.
reader = open('pg345.txt')
writer = open('pg345_cleaned.txt', 'w')

# open takes an optional parameters that specifies the “mode” – in this example,
# 'w' indicates that we’re opening the file for writing.

# As a first step, we’ll loop through the file until we find the first special line.
for line in reader:
    if is_special_line(line):
        break  # The break statement “breaks” out of the loop – that is, it causes the loop to end immediately,
        # before we get to the end of the file.

# When the loop exits, line contains the special line that made the conditional true.

print('this is the 1st special line', line)
# '*** START OF THE PROJECT GUTENBERG EBOOK DRACULA ***\n'

reader.close()
writer.close()


# Because reader keeps track of where it is in the file, we can use a second loop to pick up where we left off.
reader = open('pg345.txt')
writer = open('pg345_cleaned.txt', 'w')

for line in reader:
    if is_special_line(line):
        break
    writer.write(line)

# When this loop exits, line contains the second special line.
print('this is the second special line', line)  # seems like everytime a file was opened,
# reader will read the line from the top of a file

# '*** END OF THE PROJECT GUTENBERG EBOOK DRACULA ***\n'

# At this point, reader and writer are still open.
# To indicate that we’re done, we can close both files by invoking the close method.
writer.close()   # <-- crucial, flush buffer to disk, otherwise the new file has no content
reader.close()

# To check whether this process was successful, we can read the first few lines from the new file we just created.
# for line in open('pg345_cleaned.txt'):
#     line = line.strip()
#     if len(line) > 0:
#         print(line)
#     if line.endswith('Stoker'):  # The endswith method checks whether a string ends with a given sequence of characters.
#         break

# with block → reader.close() runs automatically
with open('pg345_cleaned.txt') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            print(line)
        if line.endswith('Stoker'):
            break

# 8.7. Find and replace

# We’ll start by counting the lines in the cleaned version of the file.

total = 0
with open('pg345_cleaned.txt') as reader:
    for line in reader:
        total += 1
        print('-', line)

print(total)


total = 0

with open('pg345_cleaned.txt') as reader:
    for line in reader:
        total += line.count('junk')

print('the number of word junk =', total)

# we can replace word junk with meaningless

# This code remove all the content in the file'pg345_cleaned.txt'
# writer = open('pg345_cleaned.txt', 'w')
# writer.close()

with open('pg345_replaced.txt', 'w') as writer, open('pg345_cleaned.txt') as reader:
    for line in reader:
        line = line.replace('junk', 'meaningless')
        print(line)
        writer.write(line)


# 8.8. Regular expressions
text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."
pattern = 'Dracula'
import re

result = re.search(pattern, text)
print(result)
# If the pattern appears in the text, search returns a Match object that contains the results of the search.
# Among other information, it has a variable named string that contains the text that was searched.

print(result.string)

# It also provides a method called group that returns the part of the text that matched the pattern.
print(result.group())

# And it provides a method called span that returns the index in the text where the pattern starts and ends.
print(result.span())

# If the pattern doesn’t appear in the text, the return value from search is None.
result = re.search('Count', text)
print(result)

# Putting all that together, here’s a function that loops through the lines in the book
# until it finds one that matches the given pattern, and returns the Match object.


def find_first(pattern):
    with open('pg345_cleaned.txt') as reader:
        for line in reader:
            result = re.search(pattern, line)
            if result != None:
                return result


result = find_first('junk')
print(result.string)

# the vertical bar character, '|', it can match either the sequence on the left or the sequence on the right.
pattern = 'junk|some'
result = find_first(pattern)
print(result.string)

# We can use a pattern like this to see how many times a character is mentioned by either name.
# Here’s a function that loops through the book and counts the number of lines that match the given pattern.

def count_matches(pattern):
    count = 0
    with open('pg345_cleaned.txt') as reader:
        for line in reader:
            result = re.search(pattern, line)
            if result != None:
                count += 1

    return count


print(count_matches('junk|some'))

# The special character '^' matches the beginning of a string, so we can find a line that starts with a given pattern.
result = find_first('some')
print(result.string)

# And the special character '$' matches the end of a string,
# so we can find a line that ends with a given pattern (ignoring the newline at the end).
result = find_first('header$')
print(result.string)


# 8.9. String substitution

pattern = 'cent(er|re)'
# In this pattern, the parentheses enclose the part of the pattern the vertical bar applies to.
# So this pattern matches a sequence that starts with 'cent' and ends with either 'er' or 're'.

# The following pattern uses the special character '?', which means that the previous character is optional.
pattern = 'colou?r'  # This pattern matches either “colour” with the 'u' or “color” without it.

# Now suppose we want to produce an edition of the book with American spellings.
# We can use the sub function in the re module, which does string substitution.
re.sub(pattern, 'color', line)  # In the result, you can see that “colour” has been replaced with “color”.

# 8.10. Debugging


# If you are working in a Jupyter notebook, you can use shell commands to help.
# For example, to display the first few lines of a file, you can use the command !head, like this:
!head pg345_cleaned.txt
# The initial exclamation point, !, indicates that this is a shell command,
# which is not part of Python.

# To display the last few lines, you can use !tail.
!tail pg345_cleaned.txt

# To make a small file that contains part of a larger file, we can use !head again with the redirect operator,
# >, which indicates that the results should be written to a file rather than displayed.

!head pg345_cleaned.txt > pg345_cleaned_10_lines.txt
# By default, !head reads the first 10 lines, but it takes an optional argument that indicates the number of lines to read.
!head -100 pg345_cleaned.txt > pg345_cleaned_100_lines.txt
# This shell command reads the first 100 lines from pg345_cleaned.txt and writes them to a file called pg345_cleaned_100_lines.txt.

# Note: The shell commands !head and !tail are not available on all operating systems. If they don’t work for you,
# we can write similar functions in Python. See the first exercise at the end of this chapter for suggestions.


# 8.11. Glossary
"""
sequence: An ordered collection of values where each value is identified by an integer index.

character: An element of a string, including letters, numbers, and symbols.

index: An integer value used to select an item in a sequence, such as a character in a string. In Python indices start from 0.

slice: A part of a string specified by a range of indices.

empty string: A string that contains no characters and has length 0.

object: Something a variable can refer to. An object has a type and a value.

immutable: If the elements of an object cannot be changed, the object is immutable.

invocation: An expression – or part of an expression – that calls a method.

regular expression: A sequence of characters that defines a search pattern.

pattern: A rule that specifies the requirements a string has to meet to constitute a match.

string substitution: Replacement of a string, or part of a string, with another string.

shell command: A statement in a shell language, which is a language used to interact with an operating system.
"""
