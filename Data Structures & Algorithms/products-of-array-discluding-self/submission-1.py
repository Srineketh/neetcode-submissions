class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        postfix_array = []
        output = []
        total_i = None
        total_j = None
        for n,i in enumerate(nums):
            if total_i == None:
                total_i = i
            else:
                total_i = total_i * i
            prefix_array.append(total_i)
            j = nums[len(nums) - 1 - n]
            if total_j == None:
                total_j = j
            else:
                total_j = total_j * j
            postfix_array.insert(0,total_j)
        for n,i in enumerate(nums):
            left = n - 1 if n != 0 else n
            right = n + 1 if (n + 1) < len(nums) else n
            if left == n:
                output.append(postfix_array[right])
            elif right == n:
                output.append(prefix_array[left])
            else:
                output.append(prefix_array[left] * postfix_array[right])
        return output
