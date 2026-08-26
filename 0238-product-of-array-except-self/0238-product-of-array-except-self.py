class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        prefix = []

        postfix = []

        i = 1
        for num in range(len(nums)):
            i *= nums[num]
            prefix.append(i)
            if len(prefix) == len(nums):
                i = 1

        for num in reversed(range(len(nums))):
            i *= nums[num]
            postfix.append(i)
            if len(postfix) == len(nums):
                i = 0
                postfix = list(reversed(postfix))

    
        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            post = postfix[i+1] if i < len(nums) - 1 else 1
            answer.append(pre*post)
        
        return(answer)
        
       


