//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maximumSumRectangle(int R, int C, vector<vector<int>> M) {
        // code here
        int maxsum = 0, mx = INT_MIN;

        int n = M.size(), m = M[0].size();

        for (int i = 0; i < m; ++i) {
            vector<int> kadane(n, 0);

            for (int j = i; j < m; ++j) {
                for (int k = 0; k < n; ++k) {
                    kadane[k] += M[k][j];
                }

                int cursum = 0;

                for (int x = 0; x < n; ++x) {
                    cursum += kadane[x];

                    mx = max(mx, kadane[x]);

                    if (cursum < 0) {
                        cursum = 0;

                    }

                    else {
                        maxsum = max(maxsum, cursum);
                    }
                }
            }
        }

        if (mx < 0) {
            return mx;
        }

        return maxsum;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, M;
        cin >> N >> M;
        vector<vector<int>> v(N, vector<int>(M));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++) cin >> v[i][j];
        Solution ob;
        cout << ob.maximumSumRectangle(N, M, v) << "\n";
    }
}
// } Driver Code Ends