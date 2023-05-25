//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int isStackPermutation(int N,vector<int> &A,vector<int> &B){
        
        stack<int> ans; int j = 0;
        for(int i = 0; i < N; i++) {
            ans.push(A[i]);
            while(!ans.empty() and j < N and ans.top() == B[j]) 
                ans.pop(), j++;
        }
        while(!ans.empty() and j < N and ans.top() == B[j])
            ans.pop(), j++;
    
        return ans.empty();
    }
};

//{ Driver Code Starts.

int main(){
    
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n),b(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for(int i=0;i<n;i++){
            cin>>b[i];
        }
        Solution ob;
        cout<<ob.isStackPermutation(n,a,b)<<endl;
    }
    
    return 0;
}
// } Driver Code Ends