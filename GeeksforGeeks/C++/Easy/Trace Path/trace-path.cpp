//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int isPossible(int n, int m, string s){
        // code here
        int x = 0, y = 0;
        int xmax = 0, xmin = 0, ymax = 0, ymin = 0;
        for (auto ch: s) {
            if (ch == 'L') {
                y = y - 1;
            } else if (ch == 'R') {
                y = y + 1;
            } else if (ch == 'D') {
                x = x - 1;
            } else {
                x = x + 1;
            }
            xmax = max(xmax, x), xmin = min(xmin, x);
            ymax = max(ymax, y), ymin = min(ymin, y);
        }
        if ((xmax - xmin + 1) <= n && (ymax - ymin + 1) <= m) {
            return true;
        } else {
            return false;
        }
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        string s;
        cin>>s;
        
        Solution ob;
        cout<<ob.isPossible(n, m, s)<<endl;
    }
    return 0;
}
// } Driver Code Ends