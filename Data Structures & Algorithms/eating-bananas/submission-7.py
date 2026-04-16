class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l<=r:
            tt = 0
            m = (l+r)//2
            for p in piles:
                tt+=math.ceil((float(p) / m))
            if tt<=h:
                r = m-1
                res = m
            else:
                l = m+1
        return res

            
        