class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            print("left index:",left)
            while left < right and not s[left].lower().isalnum():
                left += 1
            while left < right and not s[right].lower().isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        
        return True


        
            
    
        