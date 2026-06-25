class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()          # right asteroid dies
                elif stack[-1] == -a:
                    stack.pop()          # both die
                    break
                else:
                    break                # left asteroid dies
            else:
                stack.append(a)

        return stack