class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # each index represents a - z
                             # new count[] every string

            for character in s:
                count[ord(character) - ord("a")] += 1 # ascii of 'a' = 97 - 97 = index at 0
                                                      # ascii of 'b' = 98 - 97 = index at 1

            # change count to tuple because keys have to be immutable
            result[tuple(count)].append(s) # appends value s to key [0,1,0,0...]
        
        return list(result.values())