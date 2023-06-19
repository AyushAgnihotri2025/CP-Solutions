//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution{
    public:
    int count(int N, vector<int> A,int X)
    {
        // code here
        int temp=0,ans=N;
        for(int i=31;i>=0;i--){
            if((X>>i)&1){
                temp|=(1<<i);
            }
            else{
                int p=temp|(1<<i);
                int cnt=0;
                for(auto j:A){
                    if((j&p)==p)cnt++;
                }
            ans=min(ans,N-cnt);
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int N,X;
        cin>>N>>X;
        vector<int> A(N);
        for(auto &i:A)
            cin>>i;
        Solution obj;
        int ans = obj.count(N, A, X);
        cout<<ans<<endl;
    }
}
// } Driver Code Ends