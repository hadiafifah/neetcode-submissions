class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0] * 26
        s2count = [0] * 26
        matches = 0
        left = 0

        # Logic
        # We want to use an frequency counter array for each of the strings
        # matches will be initialized initially after comparing the arrays once
        # and that will be the initial matches count
        # abc, deabcf: there is an initial matches of 22 because 22 letters from a-z match
        # but 4 letters dont match, so we are comparing abc with dea initially, so only a
        # matches, and bc doesn't match, and because we also have de from s2, we have
        # 4 incorrect matches
        # if matches == 26, we get return true, else false

        if len(s1) > len(s2):
            return False

        # set the initial array for each of the letters of s1, and the first few matches
        # of s2 of length s1
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        # initialize matches
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        
        # index is the current index of the ASCII value of right
        # we want to increment s2 at the current right index to expand the window
        # if match, we increment match, if the count is over the amount of count in s1
        # we decrement matches
        # we then repeat for the left side 
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[right]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            index2 = ord(s2[left]) - ord('a')
            s2count[index2] -= 1
            if s1count[index2] == s2count[index2]:
                matches += 1
            elif s1count[index2] - 1 == s2count[index2]:
                matches -= 1

            left += 1
        return matches == 26
