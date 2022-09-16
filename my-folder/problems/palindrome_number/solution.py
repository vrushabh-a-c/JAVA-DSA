class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        temp = x
        res = 0
        while x:
            res = res*10 + x%10
            x/=10
        if temp == res:
            return True
        else:
            return False