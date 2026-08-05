class Solution(object):
    def isPalindrome(self, s):
      

        result = ""

        for ch in s.lower():
            if ch.isalnum():
                result += ch

        return result == result[::-1]