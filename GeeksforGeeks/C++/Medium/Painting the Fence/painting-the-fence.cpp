//{ Driver Code Starts
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    long long countWays(int n, int k){
        // code here
        if(n==1) return k;
        long long mod = 1e9+7;
        long long same = k * 1;
        long long diff = k * (k-1);
        long long total = same + diff;
        for(int i=3;i<=n;i++){
            same = diff * 1;
            diff = (total * (k-1))%mod;
            total=(same+diff)%mod;
        }
        return total%mod;
    }
};

//{ Driver Code Starts.

int main()
{
	
	int t;
	cin>>t;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		Solution ob;
		cout<<ob.countWays(n,k)<<endl;
	}
	return 0;
}
// } Driver Code Ends