"""66. Plus One
Easy
Topics
premium lock icon
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's."""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        op = []
        rev = 0

        for i, n in enumerate(digits[::-1]):  # # start at second last, go back to first
            if len(digits) == 1 and n + 1 == 10:  # handle the only digit cases
                op.append(0)
                rev = 1
                op.append(rev)
            elif len(digits) == 1 and n + 1 != 10:
                op.append(n + 1)
                rev = 0

            elif i == 0 and n + 1 == 10:  # handle a list's last digit that has more than one element
                op.append(0)
                rev = 1

            elif i == 0 and n + 1 != 10:
                op.append(n + 1)
                rev = 0

            elif i != len(digits) - 1 and n + rev == 10:  # check the rest elements
                op.append(0)
                rev = 1
            elif i == len(digits) - 1 and n + rev != 10:
                op.append(n + rev)
                rev = 0

            elif i == len(digits) - 1 and n + rev == 10:  # check the last elements with one more element list
                op.append(0)
                rev = 1
                op.append(rev)

            else:
                op.append(n + rev)
                rev = 0

        return op[::-1]


digits = [1, 2, 3]
print(digits[::-1])
print(digits, '\n')


op = []
last_digit = digits[-1]
rev = 0

for i, n in enumerate(digits[::-1]):  # # start at second last, go back to first
    print(n)

    if len(digits) == 1 and n + 1 == 10:  # handle only digit cases
        op.append(0)
        rev = 1
        op.append(rev)
    elif len(digits) == 1 and n + 1 != 10:
        op.append(n + 1)
        rev = 0

    elif i == 0 and n + 1 == 10:  # handle a list's last digit that has more than one element
        op.append(0)
        rev = 1
        print(i, op)
    elif i == 0 and n + 1 != 10:
        op.append(n + 1)
        rev = 0
        print(i, op)

    elif i != len(digits) - 1 and n + rev == 10:  # check the rest elements
        op.append(0)
        print(i, op)
        rev = 1
    elif i == len(digits) - 1 and n + rev != 10:
        op.append(n + rev)
        print(i, op)
        rev = 0

    elif i == len(digits) - 1 and n + rev == 10:  # check the last elements with one more element list
        op.append(0)
        rev = 1
        op.append(rev)
        print(i, op)
    else:
        op.append(n+rev)
        print(i, op)
        rev = 0


print(op[::-1])
print(digits, '\n')




"""Runtime
0
ms
Beats
100.00%
Memory
12.15
MB
Beats
91.23%
"""

