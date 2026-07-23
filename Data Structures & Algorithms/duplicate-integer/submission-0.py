class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenMap = {}
        for number in nums:
            if number not in seenMap:
                seenMap[number] = 1
            else:
                return True
        return False