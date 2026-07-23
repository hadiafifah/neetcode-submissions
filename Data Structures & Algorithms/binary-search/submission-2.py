class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # Logic
        # we want to have two pointers left and right
        # when the midway point is too small, we update left to be mid + 1
        # because any number to the left of the midway would be smaller
        # if any number is larger, we do mid - 1 because any number would be
        # bigger than the mid
        # return mid when neither is true because then we would be at the target

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1