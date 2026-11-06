"""

231. Power of Two
Easy
Topics
premium lock icon
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false


Constraints:

-231 <= n <= 231 - 1

"""

# Logic:
# 1. A power of two is a positive integer that can be expressed as 2^x,
#    where x is a non-negative integer.
# 2. Repeatedly divide n by 2 using integer division (//).
# 3. If n is odd before reaching 1, it cannot be a power of two.
# 4. If n eventually reaches 1, it is a power of two.
# 5. Handle n <= 0 separately because zero and negative numbers
#    are not powers of two.
#
# Time Complexity: O(log n) - n is halved in each iteration.
# Space Complexity: O(1) - only a fixed number of variables are used.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            else:
                n = n // 2
        return True


# Logic:
# 1. A power of two is a positive integer whose binary representation
#    contains exactly one set bit (1).
#
# 2. Subtracting 1 from n flips the rightmost set bit (1) to 0
#    and changes all bits to its right to 1.
#
# 3. The bitwise AND operation (&) compares the corresponding bits
#    of n and n - 1.
#
# 4. If n is a power of two, n & (n - 1) equals 0,
#    because there is no position where both numbers have a 1.
#
# 5. Therefore, n is a power of two if n > 0
#    and (n & (n - 1)) == 0.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
"""- Time Complexity: O(1)
- Space Complexity: O(1)"""
