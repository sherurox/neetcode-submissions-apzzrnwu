class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        if len(s) < k: return 0
        l = 0
        count = {}
        mmax=0
        res= 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            mmax = max(mmax,count[s[r]])
            while (r-l+1) - mmax >k:
                count[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res