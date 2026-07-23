class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
         I'm thinking we go through the list of strings, and simply store how much each 
         character is appearing. That can be the key in a dictionary. Hint that we got: We can
         just store this as a 26 element integer array. 

         Then what would be the value? It could simply be a list of strings that match that
         anagram key by that point.

         Then at the end, you simply iterate through the dictionary, and print all values
        '''
        results = {}

        # Go through list of strings
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char)-97] += 1
            # value is list of strings that correspond to key
            # want = access value list, and then add the current string to it
            # then, add that back to the dictionary to update the key's value
            tuple_key = tuple(key)
            string_list = results.get(tuple_key, [])
            string_list.append(string)
            results[tuple_key] = string_list
            # by the end of this, all anagram patterns will be stored as 26 bit patterns
            # as keys to a dictionary, and the values are the corresponding strings we have
        
        final = []
        for array in results.values():
            final.append(array)
        
        return final