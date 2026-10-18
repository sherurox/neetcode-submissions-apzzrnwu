class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n>m:
            return False
        t = sorted(s1)
        for i in range(m-n+1):
            if t == sorted(s2[i:i+n]):
                return True
        return False