//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h> 
using namespace std; 


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    vector<int> Kclosest(vector<int>arr, int n, int x, int k) 
    { 
        // Your code goes here
        priority_queue< pair<int, int> > pq;
        
        for(int i=0; i<n; ++i) {
            int diff = abs( arr[i] - x );
            pq.push( {diff, arr[i]} );
            if( pq.size() > k) {
                pq.pop();
            }
        }
        
        arr.clear();
        
        while( !pq.empty() ) {
            arr.emplace_back( pq.top().second );
            pq.pop();
        }
        
        sort(begin(arr), end(arr));
        
        return arr;
    }
};

//{ Driver Code Starts.

int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n,x,k;
		cin>>n>>x>>k; 
		vector <int> array(n);
		for (int i = 0; i < n; ++i)
			cin>>array[i];
        
        Solution obj;
		vector <int> result = obj.Kclosest(array, n, x, k); 
		for (int i = 0; i < result.size(); ++i)
		{
			cout<<result[i]<<" ";
		}
		cout<<"\n";
	}

	return 0; 
} 




// } Driver Code Ends