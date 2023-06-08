//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int findMin(int n, char a[]){
        // code here
        int R = 0, G = 0, B = 0;
        for(int i = 0;i < n; i++) {
            (a[i] == 'R') ? R++ : ((a[i] == 'G') ? G++ : B++);
        }
        if(R == n || G == n || B == n)
            return n;
        if(R%2 == G%2 && G%2 == B%2)
            return 2;
        return 1;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        char a[n];
        for(int i = 0;i < n;i++)
            cin>>a[i];
        
        Solution ob;
        cout<<ob.findMin(n, a)<<"\n";
    }
    return 0;
}
// } Driver Code Ends