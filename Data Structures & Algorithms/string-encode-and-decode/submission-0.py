class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        encoded = ''
        for i in range(n):
            encoded += str(len(strs[i]))+'#'+strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s): # go through whole string
            decodedString =''
            n = 0

            # get full number before '#' and put it into n
            while s[i] != '#': 
                n = n * 10 + int(s[i])
                i += 1

            i += 1 # skip '#'

            # collect n next character and put it into a string
            for j in range(n):
                decodedString += s[i]
                i += 1
            
            # put string back into list
            decoded.append(decodedString)
        return decoded
        
                    

