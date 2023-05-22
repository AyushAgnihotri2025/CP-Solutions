//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    int removals(vector<int>& arr, int k){
        //Code here
        sort(arr.begin(),arr.end());
        int i=0;
        int j=arr.size()-1;
        int ans=0;
        while(arr[j]-arr[i]>k){
            int low=lower_bound(arr.begin(),arr.end(),k+arr[i])-arr.begin();
            int high=lower_bound(arr.begin(),arr.end(),arr[j]-k)-arr.begin();
            if(arr[low]>k+arr[i])low--;
            if(j-low>high-i)i++;
            else j--;
            ans++;
        }
        return ans;
    }
};


//{ Driver Code Starts.


int main(){
    int t;
    cin>>t;
    
    while(t--){
        int n,k;
        cin>>n>>k;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        
        Solution ob;
        int ans = ob.removals(arr,k);
        
        cout<<ans<<endl;
    }
}



// } Driver Code Ends