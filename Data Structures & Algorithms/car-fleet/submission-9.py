class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        t = []
        for i in range(len(speed)):
            x = (target - position[i]) / speed[i]
            t.append((position[i],x))
        t.sort()
        while t:
            curP,curT = t.pop()
            res +=1
            while t and curT >=t[-1][1]:
                t.pop()
        return res