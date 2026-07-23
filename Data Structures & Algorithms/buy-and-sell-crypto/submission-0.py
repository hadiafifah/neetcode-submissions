class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Logic: iterate through and profit = currentMax - currentMin
        ## choose minimum between yesterday and today's stock
        ## if today is more than currentMin, profit = today - currentmin
        ## compare the profit between last largest profit and todays profit
        ## return largest profit

        currentMin = prices[0]
        maxProfit = 0
        for i in prices:
            currentMin = min(i, currentMin)
            profit = i - currentMin
            maxProfit = max(maxProfit, profit)

        return maxProfit


            