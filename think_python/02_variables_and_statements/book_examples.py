"""
2. Variables and Statements
In the previous chapter, we used operators to write expressions that perform arithmetic computations.

In this chapter, you’ll learn about variables and statements, the import statement, and the print function.
And I’ll introduce more of the vocabulary we use to talk about programs, including “argument” and “module”.
"""

# 2.1.Variables

# A variable is a name that refers to a value. To create a variable, we can write a assignment statement like this.
n = 17

# 2.2.State diagrams

# A common way to represent variables on paper is to write the name with an arrow pointing to its value.

# 2.3.Variable names
# Variable names can be as long as you like. They can contain both letters and numbers,
# but they can’t begin with a number. It is legal to use uppercase letters,
# but it is conventional to use only lower case for variable names.

# The only punctuation that can appear in a variable name is the underscore character, _.
# It is often used in names with multiple words, such as your_name or airspeed_of_unladen_swallow.

# keyword, which is a special word used to specify the structure of a program.
# Keywords can’t be used as variable names.

# 2.4.The import statement
# In order to use some Python features, you have to import them.
# For example, the following statement imports the math module.
import math
# A module is a collection of variables and functions.
# we display values like this
print(math.pi)

# To use a variable in a module, you have to use the dot operator (.)
# between the name of the module and the name of the variable.
# The math module also contains functions. For example, sqrt computes square roots.
print(math.sqrt(25))

# And pow raises one number to the power of a second number.
print(math.pow(5,2))
# two ways to raise a number to a power: we can use the math.pow function
# or the exponentiation operator, **.
# Either one is fine, but the operator is used more often than the function.

# 2.5.Expressions and statements

# An expression can be a single value, like an integer, floating-point number, or string.
# It can also be a collection of values and operators.
# And it can include variable names and function calls.
# Here’s an expression that includes several of these elements.
# 19 + n + round(math.pi) * 2

# A statement is a unit of code that has an effect, but no value.
# For example, an assignment statement creates a variable and gives it a value,
# but the statement itself has no value.
# n = 17

# Computing the value of an expression is called evaluation.
# Running a statement is called execution.

# 2.6.The print function
# print function also works with floating-point numbers and strings
print("The value of pi is approximately")
print(math.pi)
# You can also use a sequence of expressions separated by comma.
print("The value of pi is approximately", math.pi)
# Notice that the print function puts a space between the values

# 2.7.Arguments
# When you call a function, the expression in parenthesis is called an argument.
# Some can take additional arguments that are optional.
# For example, int can take a second argument that specifies the base of the number.
print(int('101',2)) # The sequence of digits 101 in base 2 represents the number 5 in base 10.
# round also takes an optional second argument, which is the number of decimal places to round off to.
print(round(math.pi, 3))

# 2.8.Comments
# it is a good idea to add notes to your programs to explain in natural language what the program is doing.
# These notes are called comments, and they start with the # symbol.
miles = 10 / 1.61     # 10 kilometers in miles

# Everything from the # to the end of the line is ignored—it has no effect on the execution of the program.
# It is reasonable to assume that the reader can figure out what the code does;
# it is more useful to explain why.

# This comment is redundant with the code and useless:
# v = 8     # assign 8 to v

# This comment contains useful information that is not in the code:
v = 8     # velocity in miles per hour

# Good variable names can reduce the need for comments,
# but long names can make complex expressions hard to read, so there is a tradeoff.

# 2.9.Debugging
"""
Three kinds of errors can occur in a program:
 syntax errors, runtime errors, and semantic errors.
  It is useful to distinguish between them in order to track them down more quickly.

Syntax error: “Syntax” refers to the structure of a program and the rules about that structure.
 If there is a syntax error anywhere in your program, Python does not run the program.
  It displays an error message immediately.

Runtime error: If there are no syntax errors in your program, it can start running.
 But if something goes wrong, Python displays an error message and stops.
  This type of error is called a runtime error. It is also called an exception
   because it indicates that something exceptional has happened.

Semantic error: The third type of error is “semantic”, which means related to meaning.
 If there is a semantic error in your program, it runs without generating error messages,
  but it does not do what you intended. Identifying semantic errors can be tricky
   because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.
"""
# 2.10.Glossary
"""
variable: A name that refers to a value.

assignment statement: A statement that assigns a value to a variable.

state diagram: A graphical representation of a set of variables and the values they refer to.

keyword: A special word used to specify the structure of a program.

import statement: A statement that reads a module file so we can use the variables and functions it contains.

module: A file that contains Python code, including function definitions and sometimes other statements.

dot operator: The operator, ., used to access a function in another module by specifying the module name followed by a dot and the function name.

evaluate: Perform the operations in an expression in order to compute a value.

statement: One or more lines of code that represent a command or action.

execute: Run a statement and do what it says.

argument: A value provided to a function when the function is called.

comment: Text included in a program that provides information about the program but has no effect on its execution.

runtime error: An error that causes a program to display an error message and exit.

exception: An error that is detected while the program is running.

semantic error: An error that causes a program to do the wrong thing, but not to display an error message.
"""
