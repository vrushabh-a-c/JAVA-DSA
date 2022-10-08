class Solution {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int dummy_row[] = new int[row];
        int dummy_col[] = new int[col];
        Arrays.fill(dummy_row,-1);
        Arrays.fill(dummy_col,-1);
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(matrix[i][j]==0){
                    dummy_row[i] = 0;
                    dummy_col[j] = 0;
                }
            }
        }
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(dummy_row[i]==0 || dummy_col[j]==0){
                    matrix[i][j]=0;
                }
            }
        }
    }
}