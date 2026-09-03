class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # okay so we want a minheap that is of size k
        # so THAT once we know that it has the k largest elements
        # the root will be the smallest of them
        # therefore being the k largest
        heap = []

        for number in nums:
            heapq.heappush(heap, number)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]
        