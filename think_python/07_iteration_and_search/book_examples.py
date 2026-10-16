# 7.Iteration and Search


# for statements to loop through the letters in a string and the words in a file
#  the in operator to check whether a letter appears in a word,
#  a programming pattern called a “linear search”.

# 7.1. Loops and strings

# a for loop that uses the range function to display a sequence of numbers.
for i in range(3):
    print(i, end=' ')  # This version uses the keyword argument end so the print function puts a space
    # after each number rather than a newline.

# can also use a for loop to display the letters in a string.
for letter in 'Gadsby':
    print(letter, end=' ')


def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False


print(has_e('Gadsby'))
print(has_e('Emma'))


# 7.2. Reading the word list

#  list of about 114,000 official crosswords;
#  that is, words that are considered valid in crossword puzzles and other word games.
file_object = open('words.txt')

# The file object provides a function called readline, which reads characters from the file
# until it gets to a newline and returns the result as a string:
# a method, which is a function associated with an object.
line = file_object.readline()
print(line)

# To remove the newline from the end of the word, we can use strip, which is a method associated with strings,
# so we can call it like this.
# strip removes whitespace characters – including spaces, tabs, and newlines – from the beginning and end of the string.
word = line.strip()
print(word)

file_object.close()

# 7.3. Updating variables

# it is legal to make more than one assignment to the same variable.
# A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

x = 5
print(x)

x = 7
print(x)

# A common kind of assignment is an update, where the new value of the variable depends on the old.
x = x + 1  # Python evaluates the expression on the right before it assigns a value to the variable on the left.
print(x)

# Before you can update a variable, you have to initialize it, usually with a simple assignment:
z = 0
z = z + 1
print(z)

# Increasing the value of a variable is called an increment; decreasing the value is called a decrement.
# Python provides augmented assignment operators that update a variable more concisely.
# For example, the += operator increments a variable by the given amount.
z += 2
print(z)

# There are augmented assignment operators for the other arithmetic operators, including -= and *=.

# 7.4. Looping and counting

total = 0

with open('words.txt') as reader:
    for line in open('words.txt'):
        word = line.strip()
        total += 1

print(total)

# We can add a second counter to the program to keep track of the number of words that contain an “e”.
total = 0
count = 0

with open('words.txt') as reader:
    for line in reader:
        word = line.strip()
        total = total + 1
        if has_e(word):
            count += 1

print(count)

# As a percentage of total, about two-thirds of the words use the letter “e”.
print(count / total * 100)

# 7.5. The in operator

# The version of has_e we wrote in this chapter is more complicated than it needs to be.
# Python provides an operator, in, that checks whether a character appears in a string.
word = 'Gadsby'
print('e' in word)


# rewrite has_e function using in operator instead of for operator
def has_e(word):
    return 'e' in word.lower()

# 7.6.Search
# a more general function called uses_any that takes a second parameter that is a string of letters.
# It returns True if the word uses any of the letters and False otherwise.


def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False


print(uses_any('banana', 'aeiou'))
print(uses_any('apple', 'xyz'))

# The structure of uses_any is similar to has_e. It loops through the letters in word and checks them one at a time.
# If it finds one that appears in letters, it returns True immediately. If it gets all the way through the loop
# without finding any, it returns False.
#
# This pattern is called a linear search.


# 7.7. Doctest

# It is also possible to use a docstring to test a function.
# Here’s a version of uses_any with a docstring that includes tests.


def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False


# Each test begins with >>>, which is used as a prompt in some Python environments
# to indicate where the user can type code.
# In a doctest, the prompt is followed by an expression, usually a function call.
# The following line indicates the value the expression should have if the function works correctly.


# To run these tests, we have to import the doctest module and run a function called run_docstring_examples
# To make this function easier to use, I wrote the following function, which takes a function object as an argument.

from doctest import run_docstring_examples


def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)


# Now we can test uses_any like this.
run_doctests(uses_any)

# If all tests pass, run_doctests displays no output – in that case, no news is good news.
#
# To see what happens when a test fails, here’s an incorrect version of uses_any.


def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False  # INCORRECT!


run_doctests(uses_any_incorrect)
# The output includes the example that failed,
# the value the function was expected to produce, and the value the function actually produced.

# 7.8. Glossary
"""
loop variable: A variable defined in the header of a for loop.

file object: An object that represents an open file and keeps track of which parts of the file have been read or written.

method: A function that is associated with an object and called using the dot operator.

update: An assignment statement that give a new value to a variable that already exists, rather than creating a new variables.

initialize: Create a new variable and give it a value.

increment: Increase the value of a variable.

decrement: Decrease the value of a variable.

counter: A variable used to count something, usually initialized to zero and then incremented.

linear search: A computational pattern that searches through a sequence of elements and stops when it finds what it is looking for.

pass: If a test runs and the result is as expected, the test passes.

fail: If a test runs and the result is not as expected, the test fails.
"""

