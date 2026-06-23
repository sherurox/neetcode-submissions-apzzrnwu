class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        x = count.most_common()
        k = len(nums)/3
        res = []
        for i in range(len(x)):
            if x[i][1]>k:
                res.append(x[i][0])
        return res
