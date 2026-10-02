class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        l,r = 0,1
        res = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                m = prices[r] - prices[l]
                res = max(m,res)
            else:
                l=r
            r+=1
        return res