//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int mod = 1000000007;
    int knots(int M, int N, int K){
        // code here
        if(K==1)
            return M*N;

        vector<long long> curr(K+1,0);
        vector<long long> prev(K+1,0);
        
        prev[0]=1;prev[1]=1;
        curr[0]=1;
        int ans=1;
        for(int i=2;i<=max(M,N);i++){
            for(int j=1;j<=K;j++){
                curr[j]=(prev[j]%mod+prev[j-1]%mod)%mod;
            }
            
            if(i==M||i==N){
                ans=(ans%mod*curr[K]%mod)%mod;
            }
            prev=curr;
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int M, N, K;
        cin>>M>>N>>K;
        
        Solution ob;
        cout<<ob.knots(M, N, K)<<"\n";
    }
    return 0;
}
// } Driver Code Ends