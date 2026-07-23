class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetterMap = {}
        tLetterMap = {}
        for char in s:
            if char in sLetterMap:
                sLetterMap[char] += 1
            else:
                sLetterMap[char] = 1
        for char in t:
            if char in tLetterMap:
                tLetterMap[char] += 1
            else:
                tLetterMap[char] = 1
        if(sLetterMap == tLetterMap):
            return True
        return False