class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        # window has shrunk so much that left == right
        # so you can return either left or right here
        return nums[left]

