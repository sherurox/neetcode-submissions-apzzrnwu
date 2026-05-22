class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack  = []
        new = []
        for i in range(len(speed)):
            new.append((position[i], speed[i]))
        new.sort(reverse = True)
        for p,s in new:
            t = (target - p) /s
            if not stack or t>stack[-1]:
                stack.append(t)
        return len(stack)

