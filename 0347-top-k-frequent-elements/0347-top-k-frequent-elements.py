class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = []

        count = dict(Counter(nums))
        sort = sorted(count, key = lambda num: count[num], reverse=True)

        for num in sort:
            if len(answer) == k:
                break
            else:
                answer.append(num)

        return(answer)

        

        


            

        

        


            

