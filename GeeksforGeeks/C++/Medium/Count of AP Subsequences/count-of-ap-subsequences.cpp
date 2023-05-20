//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
public:
    long long int count(int N, int A[]) {
            // code here
        vector<unordered_map<int, int>> dp(N);
        long long int res = 1;
        for (int end = 1; end < N; end++) {
            for (int start = 0; start < end; start++) {
                int difference = A[end] - A[start];
                int alreadyRunning = 0;
                if (dp[start].find(difference) != dp[start].end()) {
                    alreadyRunning = dp[start][difference];
                }
                dp[end][difference] += (alreadyRunning + 1);
                res += (alreadyRunning + 1);
            }
        }
        return res + N;
    }
};




//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        int a[N];
        for(int i = 0;i<N;i++)
            cin>>a[i];
        Solution ob;
        cout << ob.count(N,a) << endl;
    }
    return 0; 
}
// } Driver Code Ends