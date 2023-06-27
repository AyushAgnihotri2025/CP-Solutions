//{ Driver Code Starts
//Initial Template for C++

// {Driver code starts
#include<bits/stdc++.h>
using namespace std;

//}Driver code ends


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    
    int uglyNumber(int n)
    {
        //your code here
        if(n == 1) return 1;
        int t2 = 0, t3 = 0, t5 = 0;
        vector<int> k(n);
        k[0] = 1;
        for(int i  = 1; i < n ; i ++) {
            k[i] = min(k[t2]*2,min(k[t3]*3,k[t5]*5));
            if(k[i] == k[t2]*2) t2++;
            if(k[i] == k[t3]*3) t3++;
            if(k[i] == k[t5]*5) t5++;
        }
        return k[n-1];
    }
};



//{ Driver Code Starts.

//{Driver code starts
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        int res;
        res=ob.uglyNumber(n);
        
        cout<<res;
        cout<<"\n";    
    }
}



// } Driver Code Ends