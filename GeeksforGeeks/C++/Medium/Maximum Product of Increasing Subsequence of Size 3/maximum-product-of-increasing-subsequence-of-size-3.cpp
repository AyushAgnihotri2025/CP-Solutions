//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 


// } Driver Code Ends
// Function to find the max product subsequence of size 3
// arr: given input array
// n: size of array
// res: array which contains the output
void maxProductSubsequence(int *arr , int n, int *res)
{
	// Your code here
	if(n <= 2){
	    res[0] = res[1] = res[2] = 0;
	    return;
	}
	long long int ans = 0;
	vector<int>rightMax(n, 0);
	rightMax[n-1] = arr[n-1];
	for(int i = n-2; i>=0; i--)rightMax[i] = max(arr[i], rightMax[i+1]);
	multiset<int>s;
	s.insert(arr[0]);
    for(int i = 1; i < n-1; i++){
        s.insert(arr[i]);
        auto it = s.lower_bound(arr[i]);
        if(it != s.begin() and rightMax[i+1] > arr[i]){
            --it;
            long long int val = *it * 1LL * arr[i] * rightMax[i+1];
            if(val > ans){
                res[0] = *it, res[1] = arr[i], res[2] = rightMax[i+1];
                ans = val;
            }
        }
    }
}


//{ Driver Code Starts.

// Driver Program 
int main()
{ 
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
	
	int T;
	cin>>T;
	while(T--){
	    int num;
	    cin>>num;
	    int arr[num];
	    for(int i = 0; i<num; ++i)
	        cin>>arr[i];
	    
	    int res[3] = {0};
	    maxProductSubsequence(arr, num, res);
	    
	    if(res[0] == 0)
	        cout<<"-1" << endl;
	    else{
    	    for(int i = 0; i<3; ++i)
    	        cout<<res[i]<<" ";
    	    cout << endl;
	    }
	}
} 


// } Driver Code Ends