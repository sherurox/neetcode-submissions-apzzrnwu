class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp) 
        stack=[]
        for i,n in enumerate(temp):
            while stack and n>stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = i - stackInd    
            stack.append((n,i))
        return res
