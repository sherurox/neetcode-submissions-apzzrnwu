class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        mmax = 0
        while r < len(prices):
            if prices[r]>=prices[l]:
                t = prices[r]-prices[l]
                mmax = max(mmax,t)
            else:
                l=r
            r+=1
        return mmax
