class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sort = sorted(set(nums))
        
        print(sort)

        answer = []
        longest = 0

        for i in range(len(sort)):
            if len(answer) == 0:
                answer.append(sort[i])
            elif sort[i] == answer[-1] + 1:
                answer.append(sort[i])
            else:
                longest = max(longest, len(answer))
                answer = [sort[i]]
        
        longest = max(longest, len(answer))
        return(longest)