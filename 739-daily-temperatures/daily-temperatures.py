class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        diff = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # while the temperature stored in the stack is less than temperature at i in the array temperatures
                index = stack.pop() #  Pop the top index from the stack.
                diff[index] = i-index # Calculate the number of days until warmer temperature.
            stack.append(i) #push the numerical days into the stack 
        return diff