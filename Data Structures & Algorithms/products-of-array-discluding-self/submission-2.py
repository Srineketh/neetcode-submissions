class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = []
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[-i - 1] = postfix[-i] * nums[-i - 1]
        for i in range(0,len(nums)):
            if i == 0:
                output.append(postfix[i + 1])
            elif i == len(nums)-1:
                output.append(prefix[i - 1])
            else:
                output.append(postfix[i+1] * prefix[i-1])
        return output
