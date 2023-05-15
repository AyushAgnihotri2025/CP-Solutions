//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
#include <bits/stdc++.h>
using namespace std;
//Position this line where user code will be pasted.

class Solution{
		

	public:
	int minimumCost(int cost[], int N, int W) 
	{ 
        // Your code goes here
        vector<int> dp(W + 1,1e9);
        dp[0] = 0;
        for (int i = N - 1; i >= 0; i--) {
            dp[0] = 0;
            for (int j = i + 1; j <= W; j++) {
                if (cost[i] != -1) {
                    dp[j] = min(dp[j],dp[j-i-1]+cost[i]);
                }
            }
        }
        if (dp[W] >= 1e9) dp[W] = -1;
        return dp[W];
	} 
};


//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n, w;
        cin >> n >> w;

        int a[n];

        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.minimumCost(a, n, w) << "\n";
	     
    }
    return 0;
}
// } Driver Code Ends