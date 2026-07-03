class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            cnt = cnt + 1 if i else 0
            res = max(res,cnt)
        return res