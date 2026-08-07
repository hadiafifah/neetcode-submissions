class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for number in nums:
            counts[number] += 1

        for number in counts:
            buckets[counts[number]].append(number)
        
        for frequency in range(len(nums), 0 ,-1):
            for number in buckets[frequency]:
                res.append(number)
                if len(res) == k:
                    return res


        


