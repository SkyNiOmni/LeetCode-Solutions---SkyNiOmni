class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Tcount = Counter(t)
        Scount = Counter(s)

        for i in t:
            if len(s) != len(t):
                isAnagram = False
                break
            elif Tcount[i] != Scount[i]:
               isAnagram = False
               break
            else:
                isAnagram = True
       
        return(isAnagram)