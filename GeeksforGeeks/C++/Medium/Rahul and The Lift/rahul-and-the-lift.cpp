//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

#define mod 1000000007
long long fact[100100], ifact[100100];

class Solution {
	long long power(long long b,long long e)
	{
		long long ret=1;
		while(e)
		{
		  if(e%2)
		    ret=(ret*b)%mod;
		  b=(b*b)%mod;
		  e/=2;
		}
	    return ret;
	}

	void pre()
	{
		memset(fact, 0, sizeof(fact));
		memset(ifact, 0, sizeof(ifact));
		fact[0]=1;
		for (int i = 1; i < 100001; ++i)
		  fact[i]=(i*fact[i-1])%mod;
		ifact[100000]=power(fact[100000],mod-2);
		for (int i = 99999; i >= 0; i--)
		  ifact[i]=((i+1)*ifact[i+1])%mod;
	}
public:
	int noOfWays(int z, int n, int m){
	    // Code here
		pre();
		long long ans=(fact[z+m-2]*ifact[z-2])%mod;
		return (int)ans;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, z, m;
		cin >> z >> n >> m;
		Solution obj;
		int ans = obj.noOfWays(z, n, m);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends