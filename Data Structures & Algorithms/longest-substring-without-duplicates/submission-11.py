class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l,r = 0,1
        if len(s) == 1:
            return 1
        myset = set()
        myset.add(s[0])
        m=0
        while r<len(s):
            if s[r] not in myset:
                myset.add(s[r])
                t = len(myset)
                m = max(m,t)
                r+=1
            else:
                while s[r] in myset:
                    myset.remove(s[l])
                    l+=1
        return m
