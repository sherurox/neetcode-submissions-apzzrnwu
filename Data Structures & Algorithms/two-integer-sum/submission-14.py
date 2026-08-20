class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}
        for i,n in enumerate(nums):
            t = target - n
            if t in myset:
                return ([myset[t],i])
            else:
                myset[n] = i
        return 
        

