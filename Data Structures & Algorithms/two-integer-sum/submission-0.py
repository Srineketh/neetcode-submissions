class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fac_map = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in fac_map:
                return [fac_map[diff],i]
            fac_map[n] = i
        return []