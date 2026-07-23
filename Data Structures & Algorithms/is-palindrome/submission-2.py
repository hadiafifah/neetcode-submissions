class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        # while starting index is less than ending index
        while i<j:
            # pointer i moves forward until it hits an alphanumeric character
            # we want to check for alphanumeric because of spaces, hyphens, punctuations, etc.
            while i< j and not s[i].isalnum():
                i+=1

            # pointer j moves backwards until it hits an alphanumeric character
            while i < j and not s[j].isalnum():
                j-=1

            # lowercase the characters
            # check if the characters at index i and j are equal, if not return false
            if s[i].lower() != s[j].lower():
                return False

            # continue along the loop until i>j
            i +=1
            j -=1
        return True