class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        return False if len(x) == len(nums) else True