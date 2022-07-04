class Solution:
    def candy(self, ratings: List[int]) -> int:
        isInc = False
        currval = 0
        prev_rating = ratings[0]
        topPeak = -1
        candies = 0

        for rating in ratings:
            if rating > prev_rating:
                if not isInc:
                    isInc = True
                    currval = 1
                currval += 1
                candies += currval

            elif rating < prev_rating:
                if isInc:
                    isInc = False
                    topPeak = currval
                    currval = 0
                currval += 1
                if currval == topPeak:
                    currval += 1
                candies += currval
            
            else:
                candies += 1
                currval = 1
                isInc = True

            prev_rating = rating
        
        return candies