//{ Driver Code Starts
 
#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends
//User function template for C++
class Solution{
public:
	int stringConversion(string x, string y)
	{
	    // Your code goes here
	    int n = x.size();
	    int m = y.size();
	    vector<vector<int>> dp(n,vector<int>(m,-1));
	    for(int i=0;i<n;i++){
	        for(int j=0;j<m;j++){
	            if(toupper(x[i]) == y[j]){
	                if(i-1>=0 && j-1>=0){
	                    if(x[i] >= 'A' && x[i] <= 'Z'){
	                        dp[i][j] = dp[i-1][j-1];
	                    }
	                    else{
	                        dp[i][j] = dp[i-1][j-1] | dp[i-1][j];
	                    }
	                }
	                else {
	                    if(i == 0 && j==0) dp[i][j] = 1;
	                    else if(i == 0 && j != 0) dp[i][j] = 0;
	                    else{
	                        if(x[i] >= 'A' && x[i] <= 'Z'){
	                            for(int k=0;k<i;k++){
	                                if(x[k] >= 'A' && x[k] <= 'Z'){
	                                    dp[i][j] = 0;
	                                    break;
	                                }
	                            }
	                            if(dp[i][j] == -1) dp[i][j] = 1;
	                        }
	                        else{
	                            int count = 1;
	                            for(int k=0;k<=i;k++){
	                                if(x[k] >= 'A' && x[k] <= 'Z'){
	                                    if(x[k] == y[j] && count == 1){
	                                        count++;
	                                    }
	                                    else{
	                                        dp[i][j] = 0;
	                                        break;
	                                    }
	                                }
	                                
	                                if(dp[i][j] == -1)dp[i][j] = 1;
	                            }
	                        }
	                    }
	                }
	            }
	            else{
	                if(x[i] >= 'a' && x[i] <= 'z'){
	                    if(i-1 >= 0) dp[i][j] = dp[i-1][j];
	                    else dp[i][j] = 0;
	                }
	                else{
	                    dp[i][j] = 0;
	                }
	            }
	        }
	    }
	    return dp[n-1][m-1];
	}
};

//{ Driver Code Starts.


int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s1, s2;
   		cin >> s1 >> s2;

   		Solution ob;

   		cout << ob.stringConversion(s1, s2) << "\n";
   	}

    return 0;
}
// } Driver Code Ends