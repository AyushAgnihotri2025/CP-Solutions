//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution
{
public:
    long long minDifference(int N, vector<int> &A) {
        // code here
        long long presum[N+1];
        presum[0] = 0;
        for(int i = 1; i <= N; i++) presum[i] = presum[i-1] + A[i-1];
        long long ans = presum[N];
        for(int i = 1; i < N-2; i++) {
            pll mml = minmax(presum, 1, i+1), mmr = minmax(presum, i+2, N);
            ans = min(ans, max(mml.second, mmr.second) - min(mml.first, mmr.first));
        }
        return ans;
    }
    typedef pair<long long, long long> pll;
    pll minmax(long long pre[], int l, int r) {
        int lo = l, hi = r-1;
        long long minSum = 0, maxSum = pre[r] - pre[l-1];
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            long long lsum = pre[mid] - pre[l-1], rsum = pre[r] - pre[mid];
            if(abs(rsum - lsum) < maxSum - minSum) {
                minSum = min(lsum, rsum);
                maxSum = max(lsum, rsum);
            }
            if(lsum < rsum) lo = mid + 1;
            else hi = mid - 1;
        }
        return {minSum, maxSum};
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        vector<int> A(N);
        for(int i=0;i<N;i++){
            cin>>A[i];
        }
        Solution ob;
        long long ans = ob.minDifference(N, A);
        cout<<ans<<endl;
    }
    return 0;
} 
// } Driver Code Ends