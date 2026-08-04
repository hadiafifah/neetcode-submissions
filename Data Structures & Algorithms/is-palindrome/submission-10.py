class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. i think you just need a left pointer and a right pointer.
        then just keep moving inward until you've past each other
        2. but left and right both need to keep moving until they both
        reach an ascii character. how do we coordinate both of them at
        the same time? i think one pointer will need to wait for the
        other
        '''

        right = len(s) - 1
        left = 0

        while right > left:
            print(right)
            print(left)
            while left < right and not s[right].isalnum():
                right -= 1
            while left < right and not s[left].isalnum():
                left += 1

            if s[right].lower() != s[left].lower():
                return False

            right -= 1
            left += 1
        return True
            
    
        