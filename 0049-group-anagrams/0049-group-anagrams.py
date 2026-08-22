class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = {}

        for string in strs:
            sort = tuple(sorted(string))
            if sort not in answer:
                answer[sort] = []
            answer[sort].append(string)
        
        return(list(answer.values()))
      
                

   

            

            
