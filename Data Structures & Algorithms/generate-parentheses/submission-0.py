class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(openN,close):
            if openN == close == n:
                res.append("".join(stack))
                return
            
            if openN <n:
                stack.append("(")
                back(openN+1,close)
                stack.pop()
            
            if close <openN:
                stack.append(")")
                back(openN,close +1)
                stack.pop()
        back(0,0)
        return res
            