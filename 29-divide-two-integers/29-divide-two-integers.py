class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        q = 0
        s = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)  else 0
        dvd, dvs = abs(dividend), abs(divisor)
        while dvd >= dvs:
            i = 0
            tmp = dvs
            while dvd >= tmp:
                tmp = tmp << 1    # multiplying by 2
                i += 1
            dvd -= tmp >> 1        #dividing by 2
            q += 1 << (i - 1)      # updating quotient
        return q if s else -q
        