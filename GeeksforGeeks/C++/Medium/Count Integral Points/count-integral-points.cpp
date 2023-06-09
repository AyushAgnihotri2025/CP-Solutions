//{ Driver Code Starts


#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
  public:
    int countIntegralPoints(int x1, int y1, int x2, int y2) {
        // code here
        if (x1 == x2 && y1 == y2)
            return 0;
        if (x1 == x2) 
            return abs(y1 - y2) - 1;
        if (y1 == y2)
            return abs(x1 - x2) - 1;
        return __gcd(abs(x1 - x2), abs(y1 - y2)) - 1;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int x1,y1,x2,y2;
        
        cin>>x1>>y1>>x2>>y2;

        Solution ob;
        cout << ob.countIntegralPoints(x1,y1,x2,y2) << endl;
    }
    return 0;
}
// } Driver Code Ends