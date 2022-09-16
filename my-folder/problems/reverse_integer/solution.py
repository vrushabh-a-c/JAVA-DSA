class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if x<0:
            symbhol = -1
            x = -x
        else:
            symbhol = 1
            
        while x:
            res = res*10 + x%10
            x /= 10
        
        return 0 if res>pow(2,31) else res*symbhol