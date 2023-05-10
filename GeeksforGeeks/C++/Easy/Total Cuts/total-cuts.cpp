//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int totalCuts(int N,int K,vector<int> &A){
        // Code here
        int mx=A[0];
       if(N==1)return 0;
        for(int i=0;i<N;i++){
           int mi=INT_MAX;
           mx=max(mx,A[i]);
           int j=i+1;
           while(j<N){
               mi=min(mi,A[j]);
               j++;
           }
           if(mi+mx >= K){
              return (N-i-1);
           }
        }
        return 0;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N,K;
        cin>>N>>K;
        vector<int> A(N);
        for(int i=0;i<N;i++){
            cin>>A[i];
        }
        Solution ob;
        cout<<ob.totalCuts(N,K,A)<<endl;
    }
    return 0;
}
// } Driver Code Ends