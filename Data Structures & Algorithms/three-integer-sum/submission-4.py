class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. so we need to return all triplets that sum up to 0,
        and everything must be distinct
        2. although it seems like each number can be used in multiple
        triplets, just not multiple times in one triplet
        3. i think the solution might be similar to two sum?
        4. we could use a hash map to store the numbers, and then maybe
        iterate through two numbers at a time, seeing if the 3rd one is
        in the list of nums
        5. this works because the solution is aimed to be O(n^2)
        6. hm but O(1) space? then we cant use a hashmap..?
        7. so we can iterate through every PAIR, but how do we check
        the 3rd element?
        8. OOOH wait the hint 2 says to sort it first
        9. we can calculate the 'target' number like in
        two sum as were iterating through every possible pair
        10. then if it's sorted.. we could binary search for the 
        target? but that would make the solution N^2logN
        11. bruh the next hint 3 got me fucked up
        12. OHH WAIT I GET IT. reverse what i was thinking of before.
        from the 'target' find the PAIR. this is where 2sum comes in
        13. breh wait no im stuck again. my aha moment was just the brute
        force algorithm
        14. ok i looked at the solution because i was stuck. basically
        from the targe find the pair, but use the fact that it's sorted to
        find the pair. start from each end of the remaining list (aka       
        excluding the target), and move left pointer to right to increase
        pair sum, or right pointer to left to decrease pair sum
        15. this will produce the pair if it exists without missing     
        anything because the list is sorted
        '''
        res = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            print("i:",i)
            while left < right and left > i:
                if nums[left] + nums[right] < target: # need to increase sum
                    left += 1
                elif nums[left] + nums[right] > target: # need to decrease sum
                    right -= 1
                elif nums[left] + nums[right] == target:
                    print("sum of:",nums[i], nums[left], nums[right])
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
            