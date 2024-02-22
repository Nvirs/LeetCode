class Solution {
    public int findJudge(int n, int[][] trust) {
       int[] x = new int[n+1];
       int[] y = new int[n+1];

       for(int[] kapcsolatok : trust){
           y[kapcsolatok[0]]++;
            x[kapcsolatok[1]]++;
       } 

       for(int i = 1;i <= n; i++){
           if( x[i] == n-1 && y[i] == 0)
           {
               return i;
           }
        }
       return -1;

    }
}
