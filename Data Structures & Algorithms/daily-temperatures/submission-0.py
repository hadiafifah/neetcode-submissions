class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair:[temperature, index]
        res = [0] * len(temperatures) # essentially create the indexing here

        # Logic
        # go through temperatures and while the stack is not empty and the current
        # temperature is larger than the temperature at the stop of the stack,
        # get the stackIndex (stackI) by popping the top of the stack and calling
        # [1] from [0, 1]
        # then get the res[] at the stack index you just popped
        # and subtract that from the current index, and the res[stackI] will be the length
        # of the days like right - left in sliding window problem
        # if the temperature is smaller than the top of the stack, we just append
        
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackI = stack.pop()[1]
                res[stackI] = (index - stackI)
            stack.append([temperature, index])
        return res