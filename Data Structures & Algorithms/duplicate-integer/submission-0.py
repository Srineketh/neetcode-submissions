class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = dict()
        for i in nums:
            if dup_map.get(i) == None:
                dup_map[i] = 1
            else: 
                return True
        return False