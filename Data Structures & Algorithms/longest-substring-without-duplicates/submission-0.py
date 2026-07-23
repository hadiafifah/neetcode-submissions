class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left = 0
        longest_string = 0

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            longest_string = max(longest_string, right - left + 1)
            
        return longest_string