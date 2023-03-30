//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
    vector<int> prefixSum = {0};
    int memo[31][31];
    int rec(vector<int> &stones, int i, int j, int piles){
        if(i >= j) return 0;
        
        if(memo[i][j] != -1) return memo[i][j];
        
        int mini = INT_MAX;
        for(int k = i; k < j; k = k+piles-1){
            int tempAns = rec(stones, i, k, piles) + rec(stones, k+1, j, piles);
            mini = min(tempAns, mini);
        }
        if((j-i)%(piles-1) == 0){
            mini += prefixSum[j+1] - prefixSum[i];
        }
        
        return memo[i][j] = mini;
    }
    int mergeStones(vector<int> &stones, int n, int k) {
        // code here

        if((n-1)%(k-1) != 0) return -1;
        for(int i : stones) prefixSum.emplace_back(prefixSum.back() + i);
        memset(memo, -1, sizeof(memo));
        return rec(stones, 0, n-1, k);
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K; 
        cin >> N >> K;
        
        vector<int> stones(N);
        
        for(int i=0;i<N;i++) {
            cin>>stones[i];
        }
        
        Solution obj;
        
        cout << obj.mergeStones(stones, N, K) << endl;
        
    }
    return 0;
}
// } Driver Code Ends