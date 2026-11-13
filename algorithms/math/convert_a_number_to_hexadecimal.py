"""
405. Convert a Number to Hexadecimal
Solved
Easy
Topics
premium lock icon
Companies
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.



Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"


Constraints:

-231 <= num <= 231 - 1
"""


class Solution:
    def toHex(self, num: int) -> str:

        # 1. Handle the 32-bit representation
        hex_chars = "0123456789abcdef"

        # 2. Define hexadecimal characters
        num = num & 0xffffffff

        # 3. Handle num == 0
        if num == 0:
            return hex_chars[0]

        # 4. Extract 4 bits repeatedly
        result = []

        while num > 0:
            rev = num & 0xf

            result.append(hex_chars[rev])

            num >>= 4

        # 5. Reverse and join the result
        result.reverse()
        return ''.join(result)
