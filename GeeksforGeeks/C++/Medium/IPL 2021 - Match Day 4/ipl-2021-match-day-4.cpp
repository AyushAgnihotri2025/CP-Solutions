//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
 
class Solution
{
    public:
    // Function for finding maximum AND value.
    int maxAND (int arr[], int n)
    {
        // Your code here
        int mx = *max_element(arr, arr+n);
        int len = log2(mx)+1, ans = 0;
        for(int i=len; i>=0; i--){
            int curr = ans|(1<<i), cnt = 0;
            for(int j=0; j<n; j++){
                if((arr[j]&curr) == curr)
                    cnt += 1;
                if(cnt == 2)
                    break;
            }
            if(cnt == 2)
                ans = curr;
        }
        return ans;
    }
};

//{ Driver Code Starts.
 
// Driver function
int main()
{
    int t;
    cin>>t;//testcases
    while(t--)
    {
        int n;
        cin>>n;//input n
        int arr[n+5],i;
        
        //inserting elements
        for(i=0;i<n;i++)
        cin>>arr[i];
        Solution obj;
        //calling maxAND() function
        cout <<  obj.maxAND(arr,n)<<endl;
    }
    return 0;
}
// } Driver Code Ends