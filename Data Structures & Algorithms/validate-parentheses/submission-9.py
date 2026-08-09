class Solution:
    def isValid(self, s: str) -> bool:
        # need stack data structure to keep track of parentheses we've seen
        # need another data structure to be able to check that the pairs match
        seen = []
        pairs = {")":"(", "}":"{", "]":"["}

        for p in s:
            print("p:", p)
            print("seen:", seen)
            if p in pairs.values():
                seen.append(p)
            elif p in pairs:
                if len(seen) == 0:
                    return False
                if seen[len(seen)-1] == pairs[p]:
                    seen.pop()
                else:
                    return False
        
        print("final seen:",seen)
        print("len seen:", len(seen))

        if len(seen) > 0:
            return False
        
        return True
            
