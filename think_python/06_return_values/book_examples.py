
# 6.1. Some functions have return values

# When you call a function like math.sqrt, the result is called a return value.
import math

print(math.sqrt(42 / math.pi))

# 6.2. And some have None

# If a function doesn’t have a return statement, it returns None, which is a special value like True and False.


def repeat(word, n):
    print(word * n)  # The return value from repeat is None


# This function uses the print function to display a string, but it does not use a return statement to return a value.
result = repeat('Finland, ', 3)
print(result)  # None

# Now here’s a function similar to repeat except that has a return value.


def repeat_string(word, n):
    return word * n  # Notice that we can use an expression in a return statement, not just a variable.


line = repeat_string('Spam, ', 4)
print(line)  # Spam, Spam, Spam, Spam,

# A function like this is called a pure function because it doesn’t display anything or have any other effect
# – other than returning a value.

# 6.3. Return values and conditionals

# Code that can never run is called dead code. In general, dead code doesn’t do any harm,
# but it often indicates a misunderstanding, and it might be confusing to someone trying to understand the program.


def absolute_value_extra_return(x):
    if x < 0:
        return -x
    else:
        return x

    return 'This is dead code'


def absolute_value_wrong(x):
    if x < 0:
        return -x
    if x > 0:
        return x


print(absolute_value_wrong(0))  # None
# the function ends without hitting a return statement, which means that the return value is None


# 6.4. Incremental development

# As you write larger functions, you might find yourself spending more time debugging.
# To deal with increasingly complex programs, you might want to try incremental development,
# which is a way of adding and testing only a small amount of code at a time.

# The print statements we wrote are useful for debugging, but once the function is working, we can remove them.
# Code like that is called scaffolding because it is helpful for building the program but is not part of the final product.


# 6.5. Boolean functions

# Functions can return the boolean values True and False,
# which is often convenient for encapsulating a complex test in a function.
# For example, is_divisible checks whether x is divisible by y with no remainder.


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


print('if 6 is divisible by 4 :', is_divisible(6, 4))

# 6.6. Recursion with return values
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'this time n =', n, ', factorial ', n, '\n')

    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        print("n =", str(n), space, "this time n =", str(n), "and recurse = factorial( n - 1 =", str(n-1), ")=", "factorial(", str(n-1), ") =", str(recurse))
        result = n * recurse
        print(space, "returning factorial ( n =", str(n), ") = n * recurse =", " n * ", 'factorial(', str(n-1), ')=', str(result), "\n")
        return result

print('let us run factorial(3) \n')

print('=====================================================================================')

print(factorial(3))

print('=====================================================================================')

def factorial2(n):
    space = ' ' * (4 * n)
    print('n =', n, space, 'header of this function, this time n =', n, ', factorial ', n, ', space is 4*n =', 4*n, '\n')

    if n == 0:
        print('n =', n, space, 'return 1', ', factorial(0)= 1, the first condition in if, and this time n =', n, ', space is 4*n =', 4*n,  '\n')
        return 1
    else:
        recurse = factorial2(n-1)
        print("n =", str(n), space, "the second condition in if, this time n =", str(n), ', space is 4*n =', 4*n)
        print("n =", str(n), space, "the second condition in if,", "and recurse = factorial( n - 1 =", str(n-1), ") = ", "factorial(", str(n-1), ") =", str(recurse), ', space is 4*n =', 4*n)
        result = n * recurse
        print("n =", str(n), space, "returning ", result, ", factorial ( n =", str(n), ") = n * recurse = ", " n * ", 'factorial(', str(n-1), ') =', str(result), "the second condition in if, this time n =", str(n), "\n")
        return result

print('let us run factorial2(3) version 2.0 \n')

print('=====================================================================================')

print(factorial2(3))

print('=====================================================================================')

def factorial3(n):
    space = ' ' * (4 * n)
    print('n =', n, space, 'header,' , 'factorial ', n)

    if n == 0:
        print('n =', n, space, 'returning 1', ', factorial(0)= 1, the first condition in if, and this time n =', n, ', space is 4*n =', 4*n,'\n')
        return 1
    else:
        recurse = factorial3(n-1)
        # print("n =", str(n), space, "the second condition in if, this time n =", str(n), ', space is 4*n =', 4*n)
        # print("n =", str(n), space, "the second condition in if,", "and recurse = factorial( n - 1 =", str(n-1), ") = ", "factorial(", str(n-1), ") =", str(recurse), ', space is 4*n =', 4*n)
        result = n * recurse
        print("n =", str(n), space, "returning ", result, ", factorial ( n =", str(n), ") = n * recurse = ", " n * ", 'factorial(', str(n-1), ') =', str(result), "the second condition in if, this time n =", str(n))
        return result

print('let us run factorial3(3) version 3.0 \n')

print('=====================================================================================')

print(factorial3(3))

print('=====================================================================================')

# 6.7. Leap of faith

# When you come to a function call, instead of following the flow of execution,
# you assume that the function works correctly and returns the right result.

# 6.8. Fibonacci


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 6.9. Checking types

# Checking the parameters of a function to make sure they have the correct types and values is called input validation.

# a version of factorial with error-checking.


def factorial(n):
    if not isinstance(n, int):
        print('factorial is only defined for integers.')
        return None
    elif n < 0:
        print('factorial is not defined for negative numbers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


# 6.10. Debugging

# Breaking a large program into smaller functions creates natural checkpoints for debugging.
# If a function is not working, there are three possibilities to consider:

# There is something wrong with the arguments the function is getting – that is, a precondition is violated.
#
# There is something wrong with the function – that is, a postcondition is violated.
#
# The caller is doing something wrong with the return value.

# To rule out the first possibility,
# you can add a print statement at the beginning of the function that displays the values of the parameters
# (and maybe their types). Or you can write code that checks the preconditions explicitly.

# If the parameters look good, you can add a print statement before each return statement
# and display the return value. If possible, call the function with arguments that make it easy check the result.

# If the function seems to be working, look at the function call to make sure the return value is being used correctly – or used at all!


# 6.11. Glossary

"""
return value: The result of a function. If a function call is used as an expression, the return value is the value of the expression.

pure function: A function that does not display anything or have any other effect, other than returning a return value.

dead code: Part of a program that can never run, often because it appears after a return statement.

incremental development: A program development plan intended to avoid debugging by adding and testing only a small amount of code at a time.

scaffolding: Code that is used during program development but is not part of the final version.

Turing complete: A language, or subset of a language, is Turing complete if it can perform any computation that can be described by an algorithm.

input validation: Checking the parameters of a function to make sure they have the correct types and values
"""


