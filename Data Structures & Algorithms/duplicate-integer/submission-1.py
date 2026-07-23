class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set() # Use set instead of dictionary because I'm kinda using a little more space
        for number in nums:
            if number in seenSet: # Simplify Logic
                return True
            seenSet.add(number) # else keyword omitted
        return False