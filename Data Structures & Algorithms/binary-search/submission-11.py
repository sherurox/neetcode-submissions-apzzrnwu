class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            t = (l+r)//2
            if target < nums[t]:
                r-=1
            elif target >nums[t]:
                l+=1
            else:
                return t
        return -1