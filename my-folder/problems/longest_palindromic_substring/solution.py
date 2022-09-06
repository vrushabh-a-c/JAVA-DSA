class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            tmp = self.expand(s,i,i)
            if(len(tmp)>len(res)):
                res = tmp
            
            tmp = self.expand(s,i,i+1)
            if(len(tmp)>len(res)):
                res = tmp
        
        return res
        
    def expand(self,s,low,high):
        length = len(s)
        while low>=0 and high<length and s[low]==s[high]:
            low=low-1
            high = high+1
        return s[low+1:high]