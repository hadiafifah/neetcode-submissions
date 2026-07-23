class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string))) # lets encoder know how many characters after # to read
            res.append("#")
            res.append(string)
        return "".join(res) # turns res into a string without all the brackets and commas
        # str(res) would return a string like [a, b, c]
        # "".join(res) would return a string like abc
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # this marks the beginning of string partitions we will read

        while i < len(s):
            j = i # this marks the end of string partitions we will read
            while s[j] != '#': # read the integers until you reach '#'
                j += 1 # this is to handle double or triple digit numbers
            length = int(s[i:j]) # amount of characters to be read
            i = j + 1 # skip to after '#'
            j = i + length # skip to end of string following '#'
            res.append(s[i:j])
            i = j
        
        return res