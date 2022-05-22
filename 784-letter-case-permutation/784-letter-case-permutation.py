
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = ['#']
        for char in s:
            new_results = []
            
            if char.isalpha():
                a, b = char.lower(), char.upper()
                for x in results:
                    new_results.append(x + a)
                    new_results.append(x + b)
            else:
                a = char
                for x in results:
                    new_results.append(x + a)
            
            results = new_results
        
        return [v[1:] for v in results]