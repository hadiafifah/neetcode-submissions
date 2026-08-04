class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        suffixes = [1] * n


        for i in range(n):
            if i == 0:
                prefixes[i] = nums[i]
                suffixes[n-1] = nums[n-1]
            else:
                prefixes[i] = nums[i] * prefixes[i-1]
                suffixes[n-1-i] = nums[n-1-i] * suffixes[n-i]
        
        output = [0] * n
        for i in range(n):
            if i == 0:
                output[0] = suffixes[1]
            elif i == (n-1):
                output[n-1] = prefixes[n-2]
            else:
                output[i] = prefixes[i-1] * suffixes[i+1]
        
        return output

        