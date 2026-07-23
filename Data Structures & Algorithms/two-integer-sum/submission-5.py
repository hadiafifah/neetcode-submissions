class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # using nums= [4,5,6] target = 10
        for i in range(len(nums)):
            # at i = 0, difference = 10 - 4 = 6
            # at i = 1, difference = 10 - 5 = 5
            # at i = 2, difference = 10 - 6 = 4
            difference = target - nums[i]

            # 6 not in prevMap
            # 5 not in prevMap
            # 4 is in prevMap
            if difference in prevMap:
                # returns [0,2]
                return [prevMap[difference], i]

            # prevMap= {4:0}
            # prevMap = {5:1}

            prevMap[nums[i]] = i
        return None