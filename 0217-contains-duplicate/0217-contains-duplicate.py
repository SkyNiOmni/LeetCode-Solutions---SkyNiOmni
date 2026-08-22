class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        values = counts.values()

        for value in values:
            if value > 1:
                ContainsDuplicate = True
                break
            else:
                ContainsDuplicate = False
        
        return(ContainsDuplicate)

        
        
        


    
        
