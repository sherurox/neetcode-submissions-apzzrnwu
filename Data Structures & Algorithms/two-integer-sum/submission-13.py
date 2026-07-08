class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,n in enumerate(nums):
            t = target - n
            if t in prevmap:
                return [prevmap[t],i]
            else:
                prevmap[n] = i