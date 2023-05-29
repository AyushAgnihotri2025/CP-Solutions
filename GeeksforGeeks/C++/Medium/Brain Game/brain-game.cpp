//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	bool isPrime(int n)
	{
	    for(int i=2; i<=sqrt(n); i++)
	        if(n%i==0)
	            return false;
	   return true;
	}
	
	int primeFactor(int n) 
	{
	    int ans = 0;
        int num =n;
        for(int i=2; i<=num/2; i++)
        {
            while(n%i == 0)
            {
                ans++;
                n/= i;
            }
        }
        return ans;
    }

    bool brainGame(vector<int>nums) {
        // Code here.
        int ans=0;
        for(int num:nums){
            if(!isPrime(num))ans=ans^(primeFactor(num)-1);
        }
        return ans!=0;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<int>nums(n);
		for(int i = 0; i < n; i++)cin >> nums[i];
		Solution ob;
		bool ans = ob.brainGame(nums);
		if(ans)
			cout << "A\n";
		else cout << "B\n";
	}  
	return 0;
}
// } Driver Code Ends