class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for i in range(len(nums) + 1)] # size of length of nums

        for num in nums: # counter for each num in nums
            hashmap[num] = hashmap.get(num,0) + 1
        for num, index in hashmap.items(): # if the value of num is equal to index of bucket, append to that index
            bucket[index].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1): # decrement from length of bucket
            for num in bucket[i]: # append num in the bucket at index i
                result.append(num)
                if len(result) == k: # until the array reaches size of k
                    return result