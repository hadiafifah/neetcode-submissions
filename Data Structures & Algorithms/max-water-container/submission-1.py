class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. okay so brute force would be O(n^2). but they want O(n) time and O(1) space
        2. okay so should we do an approach similar to 3sum? 2 pointers on each end, and then move inward?
        3. so start from tail ends, compute max_water which is that, then try using next bar in
        4. if using that one creates more water, switch to that one, and then try bringing in the other bar
        5. if not, keep the old bar
        6. actually no. i looked at the solution. you move in the direction to get rid of the smaller bar
        '''
        left = 0
        right = len(heights) -1

        res = (right-left) * min(heights[right], heights[left])

        while left < right:
            if heights[left] <= heights[right]:
                left += 1 # because left is shorter, we want to get rid of it
            else:
                right -= 1
            res = max(res, (right-left)*min(heights[right], heights[left]))
        return res


        