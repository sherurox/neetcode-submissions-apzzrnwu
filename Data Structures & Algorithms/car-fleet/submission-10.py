class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i,n in enumerate(speed):
            stack.append((position[i],speed[i]))
        stack.sort(reverse=True)
        nstack = []
        for p,s in stack:
            t = ((target - p) / s)
            if not nstack or t>nstack[-1]:
                nstack.append(t)
        return len(nstack)
