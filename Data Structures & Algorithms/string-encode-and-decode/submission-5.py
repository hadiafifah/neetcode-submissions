class Solution:
    def encode(self, strs: List[str]) -> str:
        # python strings are immutable, so we use lists instead
        encoded_string = []
        for string in strs:
            length = len(string)
            encoded_string.append(str(length))
            encoded_string.append("#")
            encoded_string.append(string)
        return "".join(encoded_string)
        
        
    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        right = left = 0

        while right != len(s):
            print(right)
            while s[right] != "#":
                right += 1
            number = int(s[left:right])
            left = right + 1
            right = left + number
            string = s[left:right]
            decoded_strings.append(string)
            left = right
        
        return decoded_strings
        

        