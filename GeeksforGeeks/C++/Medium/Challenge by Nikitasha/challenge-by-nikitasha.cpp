//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    long long int findMaximum(string S,int N,int Z,int K){
        //Code Here
        const int M = 1e9 + 7;
        long long p = 1;
        for(int i = 1; i < Z; ++i) {
            p = p * K % M;
        }
        long long ans = 0;
        long long t = 0;
        for(int i = N - 1; i >= N - Z; --i) {
            t = (t * K + S[i]) % M;
        }
        ans = t;
        for(int i = N - Z - 1; i >= 0; --i) {
            t = (t + M - p * S[i+Z] % M) % M;
            t = (t * K + S[i]) % M;
            ans = max(ans, t);
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,z,k;
        cin>>n>>z>>k;
        string s;
        cin>>s;
        Solution ob;
        cout<<ob.findMaximum(s,n,z,k)<<"\n";
    }
    return 0;
}
// } Driver Code Ends