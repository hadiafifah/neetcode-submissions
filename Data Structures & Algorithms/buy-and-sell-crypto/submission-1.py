class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Two pointer logic
        ## set max profit = 0 and l,r = 0, 1
        ## while right < length of prices
        ## calculate currentprofit = right - left and get the max between itself
        ## and the current profit

        maxProfit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit



            