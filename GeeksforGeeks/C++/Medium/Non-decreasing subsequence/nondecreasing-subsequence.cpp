//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	int dp[1002][1002];
	int solve(int arr[],int i,int n,int k){
	    if(k==0)return 0;
	    if(i==n)return 1e9;
	    if(dp[i][k]!=-1){
	        return dp[i][k];
	    }
	    int temp=1e9;
	    for(int j=i+1;j<n;j++){
	        if(arr[j]>=arr[i])
	        temp=min(temp,arr[j]+solve(arr,j,n,k-1));
	    }
	    return dp[i][k]=temp;
	}
	int minSum(int arr[], int N, int K) 
	{ 
		// Your code goes here
		memset(dp,-1,sizeof(dp));
        int result=1e9;
        for(int i=0;i<=N-K;i++){
            result=min(result,arr[i]+solve(arr,i,N,K-1));
        }
        if(result>=1e9) return -1;
        return result;
	}
};

//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

        

	    Solution ob;
	    cout << ob.minSum(a, n, k) << "\n";
	     
    }
    return 0;
}


// } Driver Code Ends