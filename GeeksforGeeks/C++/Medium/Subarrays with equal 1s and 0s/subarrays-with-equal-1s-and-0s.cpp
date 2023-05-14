//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution{
  public:
    //Function to count subarrays with 1s and 0s.
    long long int countSubarrWithEqualZeroAndOne(int arr[], int n)
    {
        //Your code here
        for(int i=0;i<n;i++)
            if(arr[i] == 0)
                arr[i] = -1;

        unordered_map<int, int> mp;
        mp[0] = 1;
        int count=0;
        int sum=0;
        for(int i=0;i<n;i++) {
            sum += arr[i];
            if(mp.find(sum) != mp.end())
                count += mp[sum];
            mp[sum]++;
        }
        return count;
    }
};

//{ Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	int n,i;
	cin>>n;
	int arr[n];
	for(i=0;i<n;i++)
	cin>>arr[i];
	Solution obj;
	cout<< obj.countSubarrWithEqualZeroAndOne(arr, n)<<"\n";
	}
	return 0;
}

// } Driver Code Ends