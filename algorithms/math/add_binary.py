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

    # turn a binary string into a decimal number
    def binary_to_decimal(self, binary_string):
        rev = 0
        for i, binary in enumerate(reversed(binary_string)):
            rev += (2 ** i) * int(binary)
        return rev  # return a decimal number

    # turn a decimal number into a binary string
    def decimal_to_binary(self, decimal_number):
        rev = []
        # traditional way to accumulate remainder by using the quotient divided by two
        quotient, remainder = divmod(decimal_number, 2)
        rev.append(str(remainder))  # first binary in the top of the list
        while quotient > 0:
            quotient, remainder = divmod(quotient, 2)
            rev.append(str(remainder))

        return ''.join(rev[::-1])  # return a binary string

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = self.binary_to_decimal(a)
        y = self.binary_to_decimal(b)

        z = x + y

        string_z = self.decimal_to_binary(z)

        return string_z

    """
    Runtime
    15 ms Beats 9.71%
    Memory
    12.44 MB Beats 19.71%
    """

    # def addBinary(self, a, b):  # without other functions
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #       Runtime 14 ms Beats 9.71%
    #       Memory 12.38 MB Beats 49.34%
    #     """
    #     decimal_a = 0
    #     decimal_b = 0
    #
    #     for i, binary in enumerate(reversed(a)):
    #         decimal_a += (2 ** i) * int(binary)
    #
    #     for i, binary in enumerate(reversed(b)):
    #         decimal_b += (2 ** i) * int(binary)
    #
    #
    #     total = decimal_a + decimal_b  # a decimal number
    #
    #     # decimal to binary
    #     rev = []
    #     # traditional way to accumulate remainder by using the quotient divided by two
    #     quotient, remainder = divmod(total, 2)
    #     rev.append(str(remainder))  # first binary in the top of the list
    #     while quotient > 0:
    #         quotient, remainder = divmod(quotient, 2)
    #         rev.append(str(remainder))
    #
    #     z = ''.join(rev[::-1])  # binary in string
    #
    #     return z

a = "1010"
b = "1011"

print('class test')

print(Solution().addBinary(a, b))
print(type(Solution().addBinary(a, b)))


