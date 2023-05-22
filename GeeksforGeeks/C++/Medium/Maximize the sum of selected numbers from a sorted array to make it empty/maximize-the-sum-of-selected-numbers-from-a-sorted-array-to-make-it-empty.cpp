//{ Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 
  

// } Driver Code Ends
class Solution{
    public:
    int maximizeSum(int a[], int n) 
    {
        // Complete the function
        unordered_map<int,int>m;
        for(int i=0;i<n;i++) m[a[i]]++;
        int s=0;
        for(int i=n-1;i>=0;i--)
        {
            if(m[a[i]]>0)
            {
                s=s+a[i];
                m[a[i]]--;
                if(m[a[i]-1]>0) m[a[i]-1]--;
            }
        }
        return s;
    }
};


//{ Driver Code Starts.



int main()
{
    
    int t;cin>> t;
    while(t--)
    {
        int n;
        cin >> n;
        int arr[n];
        
        for(int i=0;i<n;i++)
            cin>>arr[i];
        sort(arr, arr+n);
        Solution ob;
        
        cout << ob.maximizeSum(arr, n) << endl;
        
        
    }

}


// } Driver Code Ends