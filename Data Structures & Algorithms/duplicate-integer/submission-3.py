class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        dupe = None
        for num in nums:
            if num == dupe:
                return True
            else:
                dupe = num
        return False