"""

202. Happy Number
Easy
Topics
premium lock icon
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""

# Mathematical property of this process:
# 1. Each number always produces the same next number.
#    (The transformation is deterministic.)
#
# 2. If a number appears again, the sequence will repeat
#    from that point onward, forming a cycle.
#
# 3. The cycle does not have to return to the original number.
#    It only needs to contain a previously visited number.
#
# Therefore, we use a set to record visited numbers.


"""
1. Convert the number into a list of digits.  done
2. Calculate the sum of the squares of the digits.  done
3. Repeat the process.
4. Return True if n == 1.
5. Return False if n has appeared before.
"""

# [list comprehension, string conversion, modulo and floor division, Set and cycle detection]
# Solution one:
class Solution(object):
    #This solution uses O(k) auxiliary space.

    def number_to_digits(self, n):
        return [int(l) for l in str(n)]

    def sum_of_squared_digits(self, digits):  #TODO: In solution 2. Use modulo and floor division in a while loop to get digits, delete the function above
        """
        digits is a list of numbers
        Calculate the sum of the squares of the digits.
        """
        return sum([n**2 for n in digits])

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        seen = set()
        while n not in seen:
            seen.add(n)  # Add n to seen if it has not appeared before.
            n = self.sum_of_squared_digits(self.number_to_digits(n))  # Update n with the sum of the squares of its digits.
            if n == 1: return True  # Return True if n reaches 1.

        return False  # Return False if a cycle is detected.



# Solution two:
class Solution(object):
    #This solution uses O(k) auxiliary space.

    def sum_of_squared_digits(self, n):
        """
        Calculate the sum of the squares of the digits using modulo and floor division.
        """
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10

        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        seen = set()
        while n not in seen:
            seen.add(n)  # Add n to seen if it has not appeared before.
            n = self.sum_of_squared_digits(n)  # Update n with the sum of the squares of its digits.
            if n == 1: return True  # Return True if n reaches 1.

        return False  # Return False if a cycle is detected.

