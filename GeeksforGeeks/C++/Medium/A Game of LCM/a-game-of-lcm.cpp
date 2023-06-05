//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    long long solve(int n, int k, vector<long long>& temp) {
        if(k == 0) {
            long long ans = temp[0];
            for(int i=1; i<4; i++) {
                ans = (ans*temp[i])/__gcd(ans, temp[i]);
            }
            return ans;
        }
        
        long long ans = LONG_MIN;
        for(int i=n; i>=n/4; i--) {
            temp.push_back(i);
            ans = max(ans, solve(n, k-1, temp));
            temp.pop_back();
        }
        
        return ans;
    }

    long long maxGcd(int N) {
        // code here
        vector<long long> temp;
        return solve(N, 4, temp);
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        Solution ob;
        cout << ob.maxGcd(N) << "\n";
    }
}
// } Driver Code Ends