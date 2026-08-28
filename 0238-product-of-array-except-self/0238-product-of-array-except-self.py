class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        prefix = []

        postfix = []

        num = 1
        for i in range(len(nums)):
            num *= nums[i]
            prefix.append(num)
            if len(prefix) == len(nums):
                num = 1

        for i in reversed(range(len(nums))):
            num *= nums[i]
            postfix.append(num)
            if len(postfix) == len(nums):
                postfix = list(reversed(postfix))

    
        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            post = postfix[i+1] if i < len(nums) - 1 else 1
            answer.append(pre*post)
        
        return(answer)
        
       



