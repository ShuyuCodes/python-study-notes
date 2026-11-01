class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
def longestCommonPrefix(strs):
    # Find the shortest word in the list
    word = ''
    for i, w in enumerate(strs):
        if i < len(strs) - 1:
            if len(w) < len(strs[i + 1]):
                word = w
    strs.remove(word)

    # Check each element in the list with the shortest word
    l = []
    flag = False
    for i in range(len(word)):
        for s in strs:
            if word[i] != s[i]:
                flag = False
            else:
                flag = True
        if flag:
            l.append(word[i])

    return ''.join(l)  # Return longest prefix


strs = ["flower", "flow", "flight"]
strs = ["dog", "rececar", "car"]
print(longestCommonPrefix(strs))
