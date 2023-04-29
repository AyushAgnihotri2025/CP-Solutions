//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    long long findNumber(long long N){
        // Code here
        int arr[] = {9, 1, 3, 5, 7};
        long long curr = 1, ans = 0;
        while(N){
            ans = arr[N%5]*curr+ans;
            if (N % 5 == 0) {
                N = N / 5 - 1;
            } else {
                N /= 5;
            }
            curr*=10;
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        long long N;
        cin>>N;
        Solution ob;
        cout<<ob.findNumber(N)<<endl;
    }
    return 0;
}
// } Driver Code Ends