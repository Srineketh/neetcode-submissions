class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = dict()
        for i in nums:
            if duplicates.get(i) != None:
                return True
            duplicates[i] = True
        return False