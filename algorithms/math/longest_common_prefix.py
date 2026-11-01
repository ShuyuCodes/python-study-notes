class Solution(object):  # LeetCode problem (Chinese website)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Find the shortest string in the list.
        word = strs[0]
        for w in strs:
            if len(w) < len(word):
                word = w

        # Compare characters at each position with the corresponding characters in all strings.
        l = []

        for i in range(len(word)):
            flag = True  # Assume all characters match at this position.

            for s in strs:
                if word[i] != s[i]:
                    flag = False
                    break  # No need to check the remaining strings.

            if flag:
                l.append(word[i])  # Add the matching character to the prefix.
            else:
                break  # Stop when the common prefix ends.

        return ''.join(l)  # Combine the matching characters into a string.


strs = ["flower", "flow", "flight"]
# strs = ["dog", "rececar", "car"]
print(Solution().longestCommonPrefix(strs))
