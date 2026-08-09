class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = { ")" : "(", "]" : "[", "}" : "{" }

        for p in s:
            if p in valid_pairs:
                # there must be something in stack AND the last thing is the correct pair
                if len(stack) != 0 and stack[-1] == valid_pairs[p]:
                    stack.pop()
                else:
                    return False
            # we can assume that the only inputs will be those 6 types of parentheses, so if its not a closing parentheses, it will be an opening one
            else:
                stack.append(p)
        
        if len(stack) == 0:
            return True
        else:
            return False

        
            
