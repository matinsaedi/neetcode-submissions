class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp_stack = []
        index_stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            if temp_stack:
                if temp_stack[-1] >= temp:
                    temp_stack.append(temp)
                    index_stack.append(i)

                else:
                    while temp_stack and temp_stack[-1] < temp:
                        output[index_stack[-1]] = i - index_stack[-1]
                        temp_stack.pop()
                        index_stack.pop()
                    
                    temp_stack.append(temp)
                    index_stack.append(i)
                        

            else:
                temp_stack.append(temp)
                index_stack.append(i)

        return output

        



        