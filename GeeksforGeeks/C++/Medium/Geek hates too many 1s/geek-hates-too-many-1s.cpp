//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {

  public:
    int noConseBits(int n) {
        // code here
        for(int i = 30; i>=2; i--)
        {
            int mask1 = 1<<i;
            int mask2 = 1<<(i-1);
            int mask3 = 1<<(i-2);
            if((mask1&n) && (mask2&n) && (mask3&n)){
                n = (n^mask3);
            }
        }
        return n;
    }
};


//{ Driver Code Starts.

int main() {

    int tt;
    cin >> tt;
    Solution sol;
    while (tt--) {

        int n;
        cin >> n;
        int ans = sol.noConseBits(n);
        cout << ans << '\n';
    }

    return 0;
}

// } Driver Code Ends