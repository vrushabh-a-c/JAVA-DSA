class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        left,right = 0,size-1
        max_width = size-1
        area = 0
        for width in range(max_width,0,-1):
            if(height[left]<height[right]):
                area = max(area,height[left]*width)
                left+=1
            else:
                area = max(area,height[right]*width)
                right-=1
                
        return area