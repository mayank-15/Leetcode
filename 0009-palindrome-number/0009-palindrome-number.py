class Solution(object):
    def isPalindrome(self,i):
    
        if i<0:
            return False
        
        str_x = str(i)
        
        return str_x==str_x[::-1]
        