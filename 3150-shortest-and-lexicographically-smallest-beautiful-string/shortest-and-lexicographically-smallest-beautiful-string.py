class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        ones = 0
        ans = None

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # Too many 1s: move left forward
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeros
            while ones == k and left < right and s[left] == '0':
                left += 1

            if ones == k:
                curr = s[left:right + 1]

                if (ans is None or
                    len(curr) < len(ans) or
                    (len(curr) == len(ans) and curr < ans)):
                    ans = curr

        return ans if ans is not None else ""