class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        k = nums.copy()
        for n in nums:
            k.append(n)
        return k