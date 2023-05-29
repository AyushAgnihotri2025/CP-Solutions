//{ Driver Code Starts


#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends

class Solution{
public:
    long long noOfDigits(int N){
        // code here
        if (N == 1)
            return 1;
        long double d = (N * log10(1.6180339887498948)) - ((log10(5)) / 2);
        return ceil(d);
    }
};



//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.noOfDigits(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends