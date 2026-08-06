class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ok so my idea is to have a dictonary where key: set of letters
        and value is list of anagrams
        actually the key cant be a set because sets are unhashable. i could
        use a tuple instead
        at the very end, iterate through everything in the dict and add      
        everything to final
        '''
        anagrams = {}

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char.lower()) - 97] += 1
            key = tuple(key)
            string_list = anagrams.get(key, [])
            string_list.append(string)
            anagrams[key] = string_list
        
        result = []
        for strings in anagrams.values():
            result.append(strings)
        
        return result
