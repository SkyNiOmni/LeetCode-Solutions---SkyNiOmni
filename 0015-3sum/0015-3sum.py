class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        answer = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            

            while left < right:
                solution = nums[i] + nums[left] + nums[right]
                if solution == 0:
                    total = [nums[i], nums[left], nums[right]]
                    answer.append(total)
                    left += 1
                    right -= 1
                    while left < right and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                elif solution < 0:
                    left += 1
                else:
                    right -= 1
                
        return(answer)