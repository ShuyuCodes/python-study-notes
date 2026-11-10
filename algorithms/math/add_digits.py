"""
258. Add Digits
Easy
Topics
premium lock icon
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1
"""
class Solution:
    def addDigits(self, num: int) -> int:
        """
                Calculate the digital root without using loops or recursion.

                Logic:
                1. The digital root is the single-digit result obtained by
                   repeatedly summing all the digits of a number.

                2. A number and the sum of its digits have the same remainder
                   when divided by 9.
                   This is because 10 % 9 = 1, 100 % 9 = 1, and so on.

                3. Therefore, we can use modulo 9 to calculate the digital root
                   directly, without repeatedly adding the digits.

                4. Special cases:
                   - If num == 0, return 0.
                   - If num > 0 and num is divisible by 9, its digital root is 9.
                   - Otherwise, its digital root is num % 9.

                5. The formula 1 + (num - 1) % 9 combines the last two cases.
                   It works for positive integers only.
                """
        if num == 0:
            return num

        return 1 + (num -1) % 9

print(Solution().addDigits(38))
print(Solution().addDigits(0))
