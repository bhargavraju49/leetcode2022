class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        k = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            s=''
            for j in i:
                s+=k[ord(j)-97]
            print(s)
            res.add(s)
        print(res)
        return len(res)
        