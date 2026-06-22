class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        x = count.most_common()
        return x[0][0]