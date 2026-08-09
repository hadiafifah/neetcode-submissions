class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # store the "last time" we saw a certain character
        left = 0 # start of window
        res = 0 # longest length

        for right in range(len(s)): # right is end of window
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right-left+1)        
        return res