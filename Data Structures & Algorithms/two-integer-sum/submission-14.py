class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Use hashmap and iterate through, and add character:index to hashmap
        ## once you get to a bigger number, 7-5 = 2 and 2 was in the hashmap from
        ## iterating through, it will be [2, current larger index]
        hashmap = {}

        for index, character in enumerate(nums):
            difference = target - character
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[character] = index