class Solution:
    def reverse(self, x: int) -> int:
        sum=0
        negative = False
        
        if x<0:
            x=x*-1
            negative=True
        while x!=0:
            sum = (sum*10) + x%10
            x=x//10

        if negative:
            sum = -sum
        if sum<-2**31 or sum>2**31-1:
            return 0
        return sum