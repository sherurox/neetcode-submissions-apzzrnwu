class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        p1,p2 = 0,0
        for t in tokens:
            if t =='+':
                p1 = stack.pop()
                p2 = stack.pop()
                res = p1 + p2
                stack.append(res)
            elif t =='-':
                p1 = stack.pop()
                p2 = stack.pop()
                res = p2-p1
                stack.append(res)
            elif t =='*':
                p1 = stack.pop()
                p2 = stack.pop()
                res = p1 * p2
                stack.append(res)
            elif t =='/':
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(p2/p1)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]