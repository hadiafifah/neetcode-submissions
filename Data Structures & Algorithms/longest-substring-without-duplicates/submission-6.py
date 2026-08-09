class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # store last index of each character
        left = 0 # start of window
        res = 0 # longest length

        for right in range(len(s)): # right is end of window
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            res = max(res, right-left + 1)
        
        return res