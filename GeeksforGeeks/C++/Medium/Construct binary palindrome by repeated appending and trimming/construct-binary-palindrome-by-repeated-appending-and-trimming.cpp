//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
public:
    string binaryPalindrome(int n,int k)
    {
       // Complete the function
       string bin(n,'0');
       int i = 0;
       while(i<n){
           bin[i] = '1';
           bin[n-i-1] = '1';
           i = i+k;
       }
       return(bin);
    }
};

//{ Driver Code Starts.
int main()
{
    int t,n,k;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        Solution obj;
        cout << obj.binaryPalindrome(n,k) << endl; 
    }
    return 0;
}

// } Driver Code Ends