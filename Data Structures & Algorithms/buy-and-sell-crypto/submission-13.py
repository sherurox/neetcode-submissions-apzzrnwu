class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res= 0
        mmax=0
        while r<len(prices):
            if prices[l]<prices[r]:
                res = prices[r]-prices[l]
                mmax = max(mmax,res)
            else:
                l=r
            r += 1
        return mmax