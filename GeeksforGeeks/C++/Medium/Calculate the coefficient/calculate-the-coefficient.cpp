//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++


class Solution{
    public:
    int permutationCoeff(int n, int k){
        //Code here
        long long MOD = 1e9+7, R = 1;
        for (int i = n; i > n - k; i--)
            R = R * i % MOD;
        return R;
    }
};


//{ Driver Code Starts.



int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        Solution ob;
        int ans = ob.permutationCoeff(n,k);
        cout<<ans<<endl;
    }
}
// } Driver Code Ends