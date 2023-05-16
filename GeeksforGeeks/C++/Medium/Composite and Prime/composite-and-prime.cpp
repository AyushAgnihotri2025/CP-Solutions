//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
	public:
		int Count(int L, int R){
		    // Code here
		    vector<bool> isprime(R+1,true);
    		  int prime=0;
    		  for(int i=2;i<=R;i++){
    		      if(isprime[i]){
    		          if(i>=L) prime++;
    		          for(int j=i+i;j<=R;j=j+i)
    		            isprime[j]=false;
    		      }
    		  }
    		  int comp=R-L+1-prime;
    		  if(L==1)
    		  return comp-prime-1;
    		  return comp-prime;
		}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int L, R;
		cin >> L >> R;
		Solution obj;
		int ans = obj.Count(L, R);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends