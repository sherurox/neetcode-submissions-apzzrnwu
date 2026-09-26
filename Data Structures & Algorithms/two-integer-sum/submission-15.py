class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i,n in enumerate(nums):
            t = target - n
            if t in mymap:
                return ([mymap[t],i])
            else:
                mymap[n] = i