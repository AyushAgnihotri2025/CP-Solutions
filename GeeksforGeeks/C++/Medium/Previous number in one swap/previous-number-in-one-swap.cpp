//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution{   
public:
    string previousNumber(string S){
        // code here 
        int large=S.length()-2;
        int small=S.length()-1;
        while(large>=0 && S[large]<=S[large+1]) large--;
        if(large<0) return "-1";
        while(small>large && S[large]<=S[small]) small--;
        while(small>0 && S[small-1]==S[small]) small--;
        char temp=S[large];
        S[large]=S[small];
        S[small]=temp;
        if(S[0]=='0') return "-1";
        return S;
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin >> S;
        Solution ob;
        cout << ob.previousNumber(S) << endl;
    }
    return 0; 
} 
// } Driver Code Ends