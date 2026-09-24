# 1.1 Arithmetic operators
# integer division, //, it always rounds to floor

print(85//2) # 42.5 but rounds to floor

# exponentiation, **, it raises a number to a power
print(7**2) # 7*7

# XOR, ^, a bitwise operator in Python. In other languages, it is exponentiation
print(7^2)

# 1.2. Expressions
# A collection of operators and numbers is called an expression.
# An expression can contain any number of operators and numbers.

#Notice that exponentiation happens before addition.
# Python follows the order of operations you might have learned in a math class:
# exponentiation happens before multiplication and division,
# which happen before addition and subtraction.

#Every expression has a value. For example, the expression 6 * 7 has the value 42.

# 1.3. Arithmetic functions

#In addition to the arithmetic operators, Python provides a few functions that work with numbers.

# the round function takes a floating-point number and rounds it off to the nearest integer.
print(round(42.4)) # 42
print(round(42.6)) # 43

#The abs function computes the absolute value of a number.

# For a positive number, the absolute value is the number itself.
print(abs(42)) # 42
print(abs(-42)) # 42

# When we use a function like this, we say we’re calling the function.
# An expression that calls a function is a function call.

#1.4. Strings
# In addition to numbers, Python can also represent sequences of letters,
# which are called strings because the letters are strung together like beads on a necklace.

# The + operator works with strings; it joins two strings into a single string, which is called concatenation
print('Well, ' + "it's a small " + 'world.')

# The * operator also works with strings; it makes multiple copies of a string and concatenates them.
print("hej "*2)

#1.5. Values and types

# Python provides a function called type that tells you the type of any value. The type of an integer is int.
print(type(2))

# The types int, float, and str can be used as functions.

# For example, int can take a floating-point number and convert it to an integer (always rounding down).
print(int(42.9))

# If you have a string that contains digits and a decimal point,
# you can use float to convert it to a floating-point number.
print(float('12.6'))

#When you write a large integer, you might be tempted to use commas between groups of digits, as in 1,000,000.
# This is a legal expression in Python, but the result is not an integer.

print(1,000,000) # Python interprets 1,000,000 as a comma-separated sequence of integers.
# You can use underscores to make large numbers easier to read.
print(1_000_000)

# 1.6. Formal and natural languages
# Natural languages are the languages people speak, like English, Spanish, and French.
# They were not designed by people; they evolved naturally.
#
# Formal languages are languages that are designed by people for specific applications.
# For example, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols.
# Similarly, programming languages are formal languages that have been designed to express computations.

#1.7. Debugging
# Programmers make mistakes. For whimsical reasons,
# programming errors are called bugs and the process of tracking them down is called debugging.

# Programming, and especially debugging, sometimes brings out strong emotions.
# If you are struggling with a difficult bug, you might feel angry, sad, or embarrassed.

# Preparing for these reactions might help you deal with them.
# One approach is to think of the computer as an employee with certain strengths, like speed and precision, and particular weaknesses,
# like lack of empathy and inability to grasp the big picture.

# 1.8. Glossary
"""
arithmetic operator: A symbol, like + and *, that denotes an arithmetic operation like addition or multiplication.

integer: A type that represents numbers with no fractional or decimal part.

floating-point: A type that represents integers and numbers with decimal parts.

integer division: An operator, //, that divides two numbers and rounds down to an integer.

expression: A combination of variables, values, and operators.

value: An integer, floating-point number, or string – or one of other kinds of values we will see later.

function: A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result.

function call: An expression – or part of an expression – that runs a function. It consists of the function name followed by an argument list in parentheses.

syntax error: An error in a program that makes it impossible to parse – and therefore impossible to run.

string: A type that represents sequences of characters.

concatenation: Joining two strings end-to-end.

type: A category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).

operand: One of the values on which an operator operates.

natural language: Any of the languages that people speak that evolved naturally.

formal language: Any of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs. All programming languages are formal languages.

bug: An error in a program.

debugging: The process of finding and correcting error
"""
