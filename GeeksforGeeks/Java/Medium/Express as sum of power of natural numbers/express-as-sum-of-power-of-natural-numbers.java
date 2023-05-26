//{ Driver Code Starts
//Initial Template for Java
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] input = new String[2]; 
            input = br.readLine().split(" "); 
            int n = Integer.parseInt(input[0]); 
            int x = Integer.parseInt(input[1]); 
            Solution ob = new Solution();
            System.out.println(ob.numOfWays(n, x));
        }
    }
}

// } Driver Code Ends


//User function Template for Java
class Solution
{
    static int numOfWays(int n, int x)
    {
        // code here
        int[][] dp=new int[n+1][n+1];
        for(int i=0;i<=n;i++){
            Arrays.fill(dp[i],-1);
        }
        return getWays(1,x,n,dp);
    }
    
    public static int getWays(int i,int x, int target,int[][] dp){
        int pow=(int)Math.pow(i,x);
        if(target==0){
            return 1;
        }
        if(pow>target){
            return 0;
        }
        if(dp[i][target]!=-1){
            return dp[i][target];
        }
        int take=getWays(i+1,x,target-pow,dp);
        int notTake=getWays(i+1,x,target,dp);
        return dp[i][target]=(take+notTake)%1000000007;
    }
}