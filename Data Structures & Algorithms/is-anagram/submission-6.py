class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            counts_s = {}
            counts_t = {}

            for char_s, char_t in zip(s, t):
                # Update counts for string s
                counts_s[char_s] = counts_s.get(char_s, 0) + 1
                
                # Update counts for string t
                counts_t[char_t] = counts_t.get(char_t, 0) + 1

            if counts_t == counts_s :
                return True

        return False