//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    long long int arrangeTiles(int N){
        // code here
        vector<long long int> dp(N+1,0);
        dp[0] = 1;
        for(int i = 1;i<dp.size();i++){
            long long int num = 0;
            if(i - 4 >=0){
                num = dp[i-4];
            }
            dp[i] = dp[i-1] + num;
        }
        return dp[N];
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        cout<<ob.arrangeTiles(N)<<"\n";
    }
    return 0;
}
// } Driver Code Ends