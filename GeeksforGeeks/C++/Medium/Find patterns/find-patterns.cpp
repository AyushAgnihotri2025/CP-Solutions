//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function template for C++

class Solution{   
public:
    int numberOfSubsequences(string S, string W){
        // code here 
        int ct = 0;
        for(int i=0;i<S.size();i++){
            int k = 0;
            for(int j=0;j<S.size();j++){
                if(W[k]==S[j]) {S[j]='?';k++;}
            }
            if(k==W.size()) ct++;
        }
        return ct;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S,W;
        cin >> S >> W;
        Solution ob;
        cout << ob.numberOfSubsequences(S,W) << endl;
    }
    return 0; 
} 


// } Driver Code Ends