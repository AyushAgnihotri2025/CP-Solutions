//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	int TotalWays(int N)
	{
	    // Code here
	    int a=1,b=1;
	    int c=1,d=1;
	    int m = 1e9+7;
	    for(int i=2;i<=N;i++)
	    {
	        c = b%m;
	        d = (a+b)%m;
	        a=c;
	        b=d;
	    }
	    long long x = c+d;
	    return (x*x)%m;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int N;
		cin >> N;
		Solution ob;
		int ans = ob.TotalWays(N);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends