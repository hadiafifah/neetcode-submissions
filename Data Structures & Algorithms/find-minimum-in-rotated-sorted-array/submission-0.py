class Solution:
    def findMin(self, nums: List[int]) -> int:

        # intuition
        # if we get the midpoint of the largest number, ie. 6//2 = 3
        # if left is more than the midpoint, we compare minimum
        # we are always finding the minimum between current min and the midpoint
        # if midpoint is larger than left, we set left = mid +1
        # if its smaller, we set right = mid -1
        
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res