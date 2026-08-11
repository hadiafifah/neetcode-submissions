class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            # if number at left less than number at right
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1
            # else if number at right is less than number at left
            else:
                # if target is less than number at mid
                # or if its greater than number at right
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1

                else:
                    left = mid + 1
        return -1
        
       