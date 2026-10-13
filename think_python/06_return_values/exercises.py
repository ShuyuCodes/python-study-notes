# 6.12. Exercises
# verbose mode

# 6.12.1. Ask a virtual assistant
import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)


# 6.12.2. Exercises

# Use incremental development to write a function called hypot that returns the length of the hypotenuse of
# a right triangle given the lengths of the other two legs as arguments.
#
# Note: There’s a function in the math module called hypot that does the same thing, but you should not use it
# for this exercise!
#
# Even if you can write the function correctly on the first try, start with a function that always returns 0
# and practice making small changes, testing as you go. When you are done, the function should only return a value – it should not display anything.


def hypot(dx, dy):
    return math.sqrt(dx**2 + dy**2)

print(hypot(3, 4))


# 6.12.3. Exercise
# Write a boolean function, is_between(x, y, z), that returns True if
#  or if
# , andFalse otherwise.

def is_between(x, y, z):
    if x < y < z or z < y < x:
        return True
    else:
        return False


print(is_between(2,3,4))
print(is_between(5,4,3))
print(is_between(6,4,8))

# 6.12.4. Exercise

# Write a function named ackermann that evaluates the Ackermann function. What happens if you call ackermann(5, 5)?


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


# print(ackermann(5, 5))  # RecursionError: maximum recursion depth exceeded

# 6.12.5. Exercise

# The greatest common divisor (GCD) of
# a and b
#  is the largest number that divides both of them with no remainder.

# One way to find the GCD of two numbers is based on the observation that if
# r is the remainder when
# a is divided by b
# , then gcd(a,b) = gcd(b, r)
# . As a base case, we can use gcd(a, 0).


# def gcd(a, b):
#     if b == 0:
#         return abs(a)
#     return gcd(b, a % b)
#
#
# print(gcd(18, 12))  # 6
# print(gcd(8, 12))   # 4

# Write a function called gcd that takes parameters a and b and returns their greatest common divisor.


def gcd(a, b):
    smallest = min(a, b)

    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(gcd(12, 18))
print(gcd(8, 12))
