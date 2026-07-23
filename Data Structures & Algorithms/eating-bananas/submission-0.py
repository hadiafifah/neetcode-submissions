class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max hours = h = 9
        # piles[i] = bananas in the pile
        # return minimum rate of eating k within h hours
        # k >= max(piles) because we can always use the largest pile which will equal to len(piles)
        # however we want to find the min k we can to eat through the bananas
        # we want to have a res variable to track the current min of eating
        # each pile has a min of 1 hour to eat

        if len(piles) > h:
            return 0
        
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left+right) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res
            