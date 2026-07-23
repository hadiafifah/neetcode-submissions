class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Logic
        # Create separate array to house calculations
        res = [1] * len(nums)

        # iterate through nums and multiply their prefix as you go along
        # ex. [1,2,4,6]
        # end result [1,1,2,8]
        prefix = 1
        for i, n in enumerate(nums):
            res[i] *= prefix
            prefix *= n

        # iterate through the nums in reverse and multiply the calculated array by the postfix as you go along
        # end result [48,24,12,8]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res