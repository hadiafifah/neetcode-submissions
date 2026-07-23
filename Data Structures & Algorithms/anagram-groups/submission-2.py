class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(string)
            # tuple(count) makes count hashable by turning it from a list to a tuple
        return list(result.values())

            