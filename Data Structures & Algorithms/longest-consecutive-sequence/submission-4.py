class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        1. what if we had some data structure that let us chain one
        element to its consecutive? then iterate through that to find
        the longest chain?
        2. that would need some kind of way to make sure that you only
        start with the smallest element in the chain, or else it
        wouldn't be an O(N) solution
        3. maybe just check if num - 1 is in nums array, then skip?
        because then that means the chain can start earlier
        4. what if we just had a dictionary? or a set? and then just
        iterated through the set, chaining
        5. wait okay so that works but then how do you iterate
        '''

        nums_set = set(nums)
        longest_chain = 0

        for number in nums_set:
            if number - 1 in nums_set:
                continue
            curr_chain = 1
            next_num = number + 1
            while next_num in nums_set:
                curr_chain += 1
                next_num += 1
            if curr_chain > longest_chain:
                longest_chain = curr_chain

        return longest_chain
