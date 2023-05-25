//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int kThSmallestFactor(int N , int K) {
        // code here
        int i = 1;
        for(i;i*i<N;i++)
        {
            if(N%i==0)
            {
                K--;
                if(K==0) return i;
            }
        }
        if(i - (N/i) == 1) i--;
    
        for(;i>=1;i--)
        {
            if(N%i==0)
            {
                K--;
                if(K==0) return (N/i);
            }
        }
        return -1;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N,K;
        
        cin>>N>>K;

        Solution ob;
        cout << ob.kThSmallestFactor(N,K) << endl;
    }
    return 0;
}
// } Driver Code Ends