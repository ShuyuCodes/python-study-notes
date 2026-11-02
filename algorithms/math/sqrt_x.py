"""
69. Sqrt(x)
Easy
Topics
premium lock icon
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 2**31 - 1
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Binary search
        if x < 2:
            return x

        left = 1
        right  = x // 2

        while left <= right:
            mid = (left + right) // 2

            if x == mid*mid:
                return mid
            # If mid is too small, exclude it and search the right half: left = mid + 1.
            # If mid is too large, exclude it and search the left half: right = mid - 1.
            # This ensures that the search range shrinks in every iteration.
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
"""
Runtime
5
ms
Beats
38.65%
Memory
12.24
MB
Beats
75.78%

"""

"""
        # Binary search
        if x == 0:
            return 0
        else:
            root = x // 2
            if root == 0:  # 1//2 = 0
                return 1
            while x < root*root:
                root = root //2
            # Floor number for root
            if x == root*root:
                return root

            # Increment floor number to find root
            for n in range(root*2, root-1, -1):
                if n*n <= x:
                    return n

Runtime
426
ms
Beats
17.00%
Memory
13.26
MB
Beats
16.60%"""
