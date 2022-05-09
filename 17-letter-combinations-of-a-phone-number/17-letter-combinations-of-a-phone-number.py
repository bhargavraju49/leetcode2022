class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def combinations(s,k,ads):
            # print('check',s,k,ads)
            if k == 0:
                res.append(ads)
                # print(ads)
                return

            for j in s[0]:
                combinations(s[1:],k-1,ads+j)
        
        k = len(digits)
        arr = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        string  = []
        for i in digits:
            string.append(arr[int(i)])
            
        
        res = []
        if k!=0:
            combinations(string,k,'')
            
        return res
        