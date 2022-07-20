class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        d = {}

        for index in range(len(s)):

            if s[index] not in d:
                d[s[index]] = [index]
            else:
                d[s[index]].append(index)

        result = []

        for word in words:

            check = 0
            current_index = -1

            for char in word:

                if char not in d:
                    break

                elif current_index > d[char][-1]:
                    break
    
                else:
        
                    for index in d[char]:
            
                        if index > current_index:
                            current_index = index
                            check = check + 1
            
                            break


                    if check == len(word):
                        result.append(word)

        return len(result)  
