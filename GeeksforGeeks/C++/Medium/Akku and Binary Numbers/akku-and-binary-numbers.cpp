//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
public:
    vector<long long>pre;  
    void precompute()
    {
        // Code Here
        for(int i=0;i<63;i++){
           for(int j=i+1;j<63;j++){
               for(int k=j+1;k<63;k++){
                   long long tmp=(1ll<<i)+(1ll<<j)+(1ll<<k);
                   pre.push_back(tmp);
               }
           }
       }
       sort(pre.begin(),pre.end());
    }
    
    long long solve(long long l, long long r){
        // Code Here
        int hi=upper_bound(pre.begin(),pre.end(),r)-pre.begin();
        int lo=lower_bound(pre.begin(),pre.end(),l)-pre.begin();
        return hi-lo;
    }
    
};



//{ Driver Code Starts.

int main()
{
    int t;
    Solution ob;
    ob.precompute();
    cin>>t;
    while(t--)
    {
        long long l,r;
        cin>>l>>r;
        cout << ob.solve(l, r) << endl; 
    }
    return 0;
}
// } Driver Code Ends