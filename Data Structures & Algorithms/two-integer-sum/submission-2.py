class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersMap = {}
        for i in range(len(nums)):
            neededNum = target - nums[i]
            if neededNum in numbersMap:
                j = numbersMap[neededNum]
                return [j, i]
            numbersMap[nums[i]] = i
        return None