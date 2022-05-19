class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split(" ")  
        s=''
        for i in k:
            s=s+i[len(i)::-1]
            s=s+' '
        return(s[:len(s)-1])