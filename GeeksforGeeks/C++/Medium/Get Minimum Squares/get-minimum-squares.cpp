//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
	public:
	int MinSquares(int n)
	{
	    // Code here
	    vector<int> a;
	    for(int i=1;i*i<=n;i++)
	     a.push_back(i*i);
	    int m=a.size();
	    vector<int> prev(n+1,1e8),curr(n+1,1e8);
	    prev[0]=0;
	    curr[0]=0;
	    for(int i=1;i<=m;i++)
	    {
	        for(int j=1;j<=n;j++)
	        {
	            if(a[i-1]<=j)
	            {
	                int take=1+curr[j-a[i-1]];
	                int notake=prev[j];
	                curr[j]=min(take,notake);
	            }
	            else
	             curr[j]=prev[j];
	        }
	        prev=curr;
	    }
	    return prev[n];
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		Solution ob;
		int ans = ob.MinSquares(n);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends