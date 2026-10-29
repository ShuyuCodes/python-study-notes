# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        original = x
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10  # x gets smaller every iteration, so it will hit 0

        return rev == original

# Follow up: Could you solve it without converting the integer to a string?
