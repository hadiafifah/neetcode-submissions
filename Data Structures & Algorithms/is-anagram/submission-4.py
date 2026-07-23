class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT= {}, {}

        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] = 1 + countS[s[i]]
            else:
                countS[s[i]] = 0
            if t[i] in countT:
                countT[t[i]] = 1 + countT[t[i]]
            else:
                countT[t[i]] = 0
        return countS == countT