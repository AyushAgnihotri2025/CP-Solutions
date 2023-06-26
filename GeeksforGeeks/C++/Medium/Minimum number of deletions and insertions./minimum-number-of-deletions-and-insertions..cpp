//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
		

	public:
	int minOperations(string str1, string str2) 
	{ 
	    // Your code goes here
	    int m = str1.size(),n = str2.size();
    vector <int> dp(n+1);
    for(int i = 1;i < m+1;i++){
        vector <int> t(n+1);
        for(int j = 1;j < n+1;j++){
            if(str1[i-1] == str2[j-1]) t[j] = dp[j-1]+1;
            else t[j] = max(t[j-1], dp[j]);
        }
        dp = t;
    }
    return n+m-(2*dp[n]);
	} 
};

//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        string s1, s2;
        cin >> s1 >> s2;

	    Solution ob;
	    cout << ob.minOperations(s1, s2) << "\n";
	     
    }
    return 0;
}


// } Driver Code Ends