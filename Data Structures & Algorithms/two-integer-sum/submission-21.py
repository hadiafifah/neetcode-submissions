class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assuming every input has exactly one pair of indicies i and j that satisfy the condition,
        # then we must also be able to assume that every integer will only appear at a single index
        log = {}

        # Iterate through nums to "log" every integer and it's index
        for index, number in enumerate(nums):
            log[number] = index
        
        print(log)

        # Iterate through nums again.
        for index, number in enumerate(nums):
            # At each number, find it's pair needed to sum up to target
            pair = target - number
            # Check if the pair exists in the log
            pair_index = log.get(pair)
            # If it does, return the number and its pair as a list
            if pair_index != None and index != pair_index:
                return [index, pair_index]

        
            

        
        