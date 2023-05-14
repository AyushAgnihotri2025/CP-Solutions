//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    long long jumpingNums(long long x) {
        // code here
        if(x <= 10) return x;
        queue<long long> q;
        for(int i = 1; i <= 9; i++) q.push(i);
        long long ans = 0;
        while(!q.empty()) {
            long long cur = q.front();
            q.pop();
            if(cur > x) continue;
            ans = max(ans,cur);
            int n = (int) cur%10;
            if(n) {
                long long t = cur*10+(n-1);
                q.push(t);
            }
            if(n != 9){
                long long t = cur*10+(n+1);
                q.push(t);
            }
        }
        return ans;
    }
};



//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long X;
        
        cin>>X;

        Solution ob;
        cout << ob.jumpingNums(X) << endl;
    }
    return 0;
}
// } Driver Code Ends