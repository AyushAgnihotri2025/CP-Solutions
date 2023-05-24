//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
#define lli long long int
#define vvi vector<vector<lli>>
#define vi  vector<lli>
#define mod 1000000007

class Solution{
public:
    long long recFunc(int n , int m , int r, vvi &dp){
        if(n == 0) return 1;
        if(dp[n][m] != -1) return dp[n][r];
        long long sum = 0;
        for(int i = 1 ; i <= m ; i++){
            if(r % i == 0 || i % r == 0) {
                sum += recFunc(n-1 , m , i , dp);
                sum %= mod;
            }
        }
        dp[n][r] = sum;
        return dp[n][r];
    }
    long long count(long long N, long long M)
    {
        // code here
       vvi dp(N+1 , vi (M+1 , -1));
       return recFunc(N , M , 1 , dp);
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        long long N,M;
        cin>>N>>M;
        Solution ob;
        cout << ob.count(N,M) << endl;
    }
    return 0; 
}
// } Driver Code Ends