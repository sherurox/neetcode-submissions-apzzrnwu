class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l<=r:
            m = (l +r)//2
            t=0
            for p in piles:
                t += math.ceil(float(p)/m)
            if t<=h:
                r = m-1
                res = m
            else:
                l=m+1
        return res