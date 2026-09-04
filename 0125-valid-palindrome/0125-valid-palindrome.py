class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        letters = []

        for i in s:
            if i.isalnum() == True:
                letters.append(i)

        letters = list(map(str,"".join(letters).lower()))

        if letters == letters[::-1]:
            return(True)
        else:
            return(False)

