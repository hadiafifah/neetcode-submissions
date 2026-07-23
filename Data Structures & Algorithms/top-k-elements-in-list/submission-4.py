class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        use bucket sort algorithm to create n buckets, grouping numbers based on their 
        frequencies from 1 to n.

        then pick the top k numbers from the buckets, starting from n down to 1
        '''

        # note: i dont need to make these buckets using a dict, a list of arrays should be fine too


        counts = {}
        for number in nums:
            counts[number] = counts.get(number, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for number in nums:
            if number not in buckets[counts[number]]:
                buckets[counts[number]].append(number)
        
        print("buckets size: "+str(len(buckets)))
        print("original nums size: "+str(len(nums)))
        print("buckets:",buckets)

        result = []
        count = 0
        i = 0
        while count != k:
            if buckets[len(nums)-i] != []:
                for elm in buckets[len(nums)-i]:
                    result.append(elm)
                    count += 1
            i += 1

        
        # for i in range(k):
        #     print("i:",i)
        #     # access buckets[n-i] if != [], then for each element in that bucket, add it to final list
        #     if buckets[len(nums)-i] != []:
        #         for elm in buckets[len(nums)-i]:
        #             result.append(elm)
        
        return result