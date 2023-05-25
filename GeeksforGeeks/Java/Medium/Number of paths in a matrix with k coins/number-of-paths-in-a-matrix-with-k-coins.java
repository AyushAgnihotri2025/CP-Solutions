//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            
            int  K = Integer.parseInt(read.readLine());
            int  N = Integer.parseInt(read.readLine());
            int arr[][] = new int[N][N];
            String input_line1[] = read.readLine().trim().split("\\s+");
            int c = 0;
            for(int i=0;i<N;i++){
                for(int j = 0;j<N;j++){
                    arr[i][j] = Integer.parseInt(input_line1[c]);
                    c++;
                }
            }
            Solution obj = new Solution();
            System.out.println(obj.numberOfPath(N, K, arr));
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    static int numberOfPathsWithKCoins = 0;
    static long dp[][][];
    long numberOfPath(int N, int K, int [][]arr) {
        // code here
        dp = new long[N][N][K+1];
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                for(int l=0;l<=K;l++)
                  dp[i][j][l]=-1;
                  
        return dfs(0, 0, N, K, 0, arr);
    }
    
    long dfs(int i, int j, int N, int K, int currentCoins, int arr[][]) {
        
        if(i < 0 || i >=N || j < 0 || j >= N || currentCoins+arr[i][j] > K) return 0;
        
        if(currentCoins+arr[i][j] == K && i == N-1 && j == N-1) {
            //System.out.println(currentCoins);
            return 1;
        }
        
        if(dp[i][j][currentCoins] != -1) return dp[i][j][currentCoins];
        
        dp[i][j][currentCoins] = dfs(i+1, j, N, K, currentCoins + arr[i][j], arr) 
            + dfs(i, j+1, N, K, currentCoins + arr[i][j], arr);
        return dp[i][j][currentCoins];
    }
}