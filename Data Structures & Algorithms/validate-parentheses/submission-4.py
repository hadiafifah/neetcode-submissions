class Solution:
    def isValid(self, s: str) -> bool:
        p_key = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i in p_key:
                if stack and stack[-1] == p_key[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False