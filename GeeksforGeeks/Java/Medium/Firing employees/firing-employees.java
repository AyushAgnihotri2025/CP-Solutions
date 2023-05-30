//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[]) throws IOException { 
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t > 0){
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; ++i)
                arr[i] = sc.nextInt();
            Solution ob = new Solution();
            System.out.println(ob.firingEmployees(arr,n));
            t--;
        }
    } 
} 
// } Driver Code Ends


//User function Template for Java

class Solution {
    static int dp[];
    static int helper(int arr[], int i){
        if(dp[i]!=-1) return dp[i];
        if(arr[i]==0) return 1;
        int val = helper(arr,arr[i]-1);
        return dp[i]=val+1;
    }
    static int firingEmployees(int arr[], int n) { 
        // code here
        boolean isPrime[] = new boolean[2*n+1];
        Arrays.fill(isPrime,true);
        for(int i=2; i*i<=2*n; i++){
            if(isPrime[i]){
                for(int j=i*i; j<=2*n; j+=i){
                    isPrime[j]=false;
                }
            }
        }
        
        dp = new int[n];
        Arrays.fill(dp,-1);

        int cnt=0;
        for(int i=0; i<n; i++){
            if(arr[i]==0) continue;
            int val = i+helper(arr,i);
            if(isPrime[val]) cnt++;
        }
        return cnt;
    } 
}