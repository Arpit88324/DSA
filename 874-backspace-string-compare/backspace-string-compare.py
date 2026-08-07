class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []

        for i in range(len(s)):
            if s[i].isalpha() :
                stack1.append(s[i])
            
            elif stack1:
                stack1.pop()
        
        for i in range(len(t)):
            if t[i].isalpha():
                stack2.append(t[i])
            elif stack2:
                stack2.pop()
        return stack1 == stack2