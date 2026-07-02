class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        postfix_array = []
        output = []
        total = None
        for i in nums:
            if total == None:
                total = i
            else:
                total = total * i
            prefix_array.append(total)
        total = None
        for i in range(len(nums)):
            j = nums[len(nums) - 1 - i]
            if total == None:
                total = j
            else:
                total = total * j
            postfix_array.insert(0,total)

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
