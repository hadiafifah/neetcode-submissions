class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_set = set()
        for number in nums:
            if number in has_set:
                return True
            else:
                has_set.add(number)
        return False
