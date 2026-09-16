class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for n,i in enumerate(nums):
            num_dict[i] = n

        for i,n in enumerate(nums):
            other_index = target - n
            if other_index in num_dict and num_dict[other_index]!= i:
                return[i,num_dict[other_index]]
        return []