class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        j = 0
        while j < k:
            result.append(max(hashmap, key=hashmap.get))
            del hashmap[result[j]]
            j += 1

        return result