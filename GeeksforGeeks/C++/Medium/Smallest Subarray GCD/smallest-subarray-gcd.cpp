//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution{   
public:
    int findSmallestSubArr(int arr[], int n, int g) {
        // code here
        int ans = -1;
        for(int i = 0;i<n;i++){
            if(arr[i]==g) return 1;
        }
        for(int i = 1;i<n;i++){
            int some = __gcd(arr[i],arr[i-1]);
            if(some==g) return 2;
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, g;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cin >> g;
        Solution ob;
        auto ans = ob.findSmallestSubArr(arr, n, g);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends