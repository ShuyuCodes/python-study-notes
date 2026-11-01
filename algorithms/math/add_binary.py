"""
67. Add Binary
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimal_a = 0
        decimal_b = 0
        for n in (a, b):
            if n == '0':
                rev = 0
                for i, binary in enumerate(reversed(a)):
                    rev += (2 ** i) * int(binary)
                decimal_a += rev
            elif n == '1':
                rev = 0
                for i, binary in enumerate(reversed(b)):
                    rev += (2 ** i) * int(binary)
                decimal_b += rev

        sum = decimal_a + decimal_b  # a decimal number


        # decimal to binary
        rev = []
        # traditional way to accumulate remainder by using the quotient divided by two
        quotient, remainder = divmod(sum, 2)
        rev.append(str(remainder))  # first binary in the top of the list
        while quotient > 0:
            quotient, remainder = divmod(quotient, 2)
            rev.append(str(remainder))

        z = ''.join(rev[::-1])  # binary in string

        return z

#
# # turn a binary string into a decimal number
# def binary_to_decimal(binary_string):
#     rev = 0
#     for i, binary in enumerate(reversed(binary_string)):
#         rev += (2**i)*int(binary)
#     return rev
#
# # turn a decimal number into a binary string
# def decimal_to_binary(decimal_number):
#     rev = []
#     # traditional way to accumulate remainder by using the quotient divided by two
#     quotient, remainder = divmod(decimal_number, 2)
#     rev.append(str(remainder))  # first binary in the top of the list
#     while quotient > 0:
#         quotient, remainder = divmod(quotient, 2)
#         rev.append(str(remainder))
#
#     return ''.join(rev[::-1])
#
#
# def addBinary(a, b):
#     """
#     :type a: str
#     :type b: str
#     :rtype: str
#     """
#     x = binary_to_decimal(a)
#     y = binary_to_decimal(b)
#
#     z = x + y
#
#     string_z = decimal_to_binary(z)
#
#     return string_z
#
#
#
# print(type(addBinary(a, b)))


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    decimal_a = 0
    decimal_b = 0
    for binary_string in (a, b):
        if binary_string == a :
            rev = 0
            for i, binary in enumerate(reversed(a)):
                rev += (2 ** i) * int(binary)
            decimal_a += rev
        elif binary_string == b:
            rev = 0
            for i, binary in enumerate(reversed(b)):
                rev += (2 ** i) * int(binary)
            decimal_b += rev

    sum = decimal_a + decimal_b  # a decimal number

    # decimal to binary
    rev = []
    # traditional way to accumulate remainder by using the quotient divided by two
    quotient, remainder = divmod(sum, 2)
    rev.append(str(remainder))  # first binary in the top of the list
    while quotient > 0:
        quotient, remainder = divmod(quotient, 2)
        rev.append(str(remainder))

    z = ''.join(rev[::-1])  # binary in string

    return z

a = "1010"
b = "1011"

print(type(addBinary(a, b)))
print(addBinary(a, b))
