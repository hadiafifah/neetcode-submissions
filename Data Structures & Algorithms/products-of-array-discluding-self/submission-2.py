class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_array = [1] * n
        prefix_array[0] = nums[0]

        suffix_array = [1] * n
        suffix_array[n-1] = nums[n-1]

        for i in range(1, n):
            prefix_array[i] = prefix_array[i-1] * nums[i]
            suffix_array[n-i-1] = suffix_array[n-i] * nums[n-i-1]
        
        print("suffix array:", suffix_array)
        print("prefix array:", prefix_array)

        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = suffix_array[1]
            elif i == n-1:
                res[i] = prefix_array[n-2]
            else:
                res[i] = prefix_array[i-1] * suffix_array[i+1]

        return res
        