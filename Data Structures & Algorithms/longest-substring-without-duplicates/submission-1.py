class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left = 0
        longest_string = 0

        # Logic:
        # for every i (right) in size of the string
        # we add it to the set unless it's already in the set
        # if its in the set then we remove the values on the left
        # of the hashset until it reaches the current value of the string
        # then we get the largest substring between previous largest
        # and the current longest

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            longest_string = max(longest_string, right - left + 1)
            
        return longest_string