class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        # Logic
        # Iterate through nums and if value not in nums
        # set length = 1 so it gets the longest sequence from each value
        # then we get the longest length from each starting each starting sequence
        
        for i in nums:
            if (i-1) not in hashset:
                length = 1
                while (i + length) in hashset:
                    length += 1
                longest = max(longest, length)
        return longest
