class Solution:
    def reverse(self, x: int) -> int:
        #32 bit signed interger is a string of 32 zeros and ones
        # largest 
        
        num = str(x) # converts int to string
        
        if '-' in num:
            idx = num.index('-')
            num = num[:idx] + num[idx+1:] 
            sign = -1 #check for negative symbol in string
        else:
            sign = 1
        
        rev = "" # contains reverse of num
        
        rev = num[::-1]
            
        rev_int = int(rev) * sign
        
        
        if rev_int >-2**31 and rev_int < (2**31-1):# if reversed interger in within range return int
            return rev_int
        else:
            return 0
            
            