class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]