class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor > 2**31 - 1 or dividend//divisor < -2**31:
            return( 2**31) - 1
        if dividend%divisor==0 or dividend//divisor>=0:
            return dividend//divisor
        else:
            return dividend//divisor + 1
        