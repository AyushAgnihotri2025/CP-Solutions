//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	vector<int> fact;
	vector<int> res;
	int F(int n){
	    if(n < 0) return -1;
	    if(n == 0) return 1;
	    for(int i = 9; i >= 0; i--){
	        int temp = F(n-fact[i]);
	        if(temp == 1){
	            res.push_back(i);
	            return 1;
	        }
	    }
	}
	vector<int> FactDigit(int N)
	{
	    // Code here
	    fact.assign(10, 1);
	    fact[0] = 1;
	    for(int i = 1; i < 10; i++){
	        fact[i] = fact[i-1] * i;
	    }
	    F(N);
	    return res;
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
		vector<int>ans = ob.FactDigit(N);
		for(auto i: ans)
			cout << i;
		cout << "\n";
	}  
	return 0;
}
// } Driver Code Ends