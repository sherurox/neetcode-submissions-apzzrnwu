class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        n = len(temp)
        for i in range(len(temp)):
            j = i+1
            while j<n and temp[j]<=temp[i]:
              j+=1
            if j<n:
                res[i] = j-i
            else:
                res[i] = 0   
        return res
