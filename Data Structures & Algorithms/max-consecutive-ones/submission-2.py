class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons_ones = []
        counter = 0
        for i in nums:
            if i != 0:
                counter += 1
            else:
                cons_ones.append(counter)
                counter = 0
        cons_ones.append(counter)
        return max(cons_ones)