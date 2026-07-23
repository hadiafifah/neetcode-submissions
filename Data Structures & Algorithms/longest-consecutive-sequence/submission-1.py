class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set()

        for i in range(n):
            numset.add(nums[i])
            
        bestlen = 0
        for x in numset:
            if x-1 not in numset:
                y = x+1
                leng = 1
                bestlen = max(bestlen, leng)
                while y in numset:
                    leng = leng + 1
                    bestlen = max(bestlen, leng)
                    y = y + 1
                    
        return bestlen