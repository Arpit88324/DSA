class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first[i]:
                    return prefix
            prefix += first[i]


        return prefix