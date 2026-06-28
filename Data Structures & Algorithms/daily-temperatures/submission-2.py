class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                index = stack[-1][0]
                output[index] = i - index
                
                stack.pop()
                        
            stack.append([i, temp])

        return output