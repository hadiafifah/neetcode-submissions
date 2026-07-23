class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        currentOp = 0

        # Logic
        # There will always be two values in the stack
        # We want to append to stack and if we hit an operator
        # we want to perform the operations on the two values in the stack
        # we perform operations on the two popped values and append the result
        # after, another value will be added onto the stack then we will hit
        # another operator and repeat

        for i in range(0, len(tokens)):
            if tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]