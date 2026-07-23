class Solution:
    # Logic
    # Just get the length of the string followed by pound followed by the string
    # and add it to a string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    # Logic
    # We set j = i, which the start of the string until j reaches #
    # We then get the length which is from i to j
    # We do this because what if the string is a two digits? we would would
    # more than one number
    # We then append the string from inclusive j to inclusive j to the length of the string
    # then we set i to the end of the string and so on
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res