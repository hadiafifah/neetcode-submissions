class Solution:
    def encode(self, strs: List[str]) -> str:
        # list of strings to a single string
        # each char in this new string will be element in list until we .join everything together
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)))
            encoded_string.append('#')
            encoded_string.append(string)
        return "".join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        # read numbers up until #
        # read x amount of characters after #
        # repeat
        l = r = 0
        decoded_strings = []

        while r < len(s):
            while s[r] != "#":
                r += 1
            # by this point, r points to #, and l points to first digit of number
            number = int(s[l:r])
            # left needs to point to first character of substring
            l = r + 1
            # right needs to point to one character AFTER last character of substring
            r = r + 1 + number # OR just do (r = l + number)
            string = s[l:r]
            decoded_strings.append(string)
            l = r
        
        return decoded_strings
            

        
        

        