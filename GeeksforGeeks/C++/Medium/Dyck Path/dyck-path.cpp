//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
  public:
    long long dyckPaths(int N) {
        // code here
        long long double_combination = 1; 
        
        for (int i = 0; i < N; ++i) 
        { 
            double_combination *= (2*N-i); 
            double_combination /= (i+1); 
        } 
    
        return double_combination/(N+1);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;

        Solution ob;
        cout << ob.dyckPaths(N) << endl;
    }
    return 0;
}
// } Driver Code Ends