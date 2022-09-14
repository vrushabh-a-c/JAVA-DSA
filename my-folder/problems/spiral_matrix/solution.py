class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        row_begin,col_begin = 0,0
        row_end = len(matrix)-1
        col_end = len(matrix[0])-1
        
        while(row_begin<=row_end and col_begin<=col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin+=1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end-=1
            
            if row_begin<=row_end:
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end-=1
            
            if col_begin<=col_end:
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin+=1
                
        return res