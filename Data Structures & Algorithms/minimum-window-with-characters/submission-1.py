class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_dict, s_dict = defaultdict(int), defaultdict(int)
        for char in t:
            t_dict[char] += 1
        
        have, need = 0, len(t_dict)
        result, result_length = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            s_dict[char] += 1

            if char in t_dict and s_dict[char] == t_dict[char]:
                have += 1

            while have == need:
                if (r - l + 1) < result_length:
                    result = [l,r]
                    result_length = r - l + 1
                
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1

        l, r = result

        if result_length != float("infinity"):
            return s[l:r+1] 
        else:
            return ""