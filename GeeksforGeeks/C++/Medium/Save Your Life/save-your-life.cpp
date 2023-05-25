//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
      string maxSum(string w,char x[], int b[],int n){
        // code here
        int len = w.length();
        vector<int> nums(len);
        map<char, int> mp;
        for(int i=0;i<n;i++){
            mp[x[i]] = b[i];
        }
        for(int i=0;i<len;i++){
            if(mp.find(w[i]) == mp.end()){
                nums[i] = int(w[i]);
            }
            else{
                nums[i] = mp[w[i]];
            }
        }
        int sum = 0, mx = INT_MIN;
        string ans = "", res;
        for(int i=0;i<len;i++){
            sum += nums[i];
            ans += w[i];
            
            if(sum > mx){
                mx = sum;
                res = ans;
            }
            
            if(sum < 0){
                sum = 0;
                ans = "";
            }
        }
        return res;
      }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string w;
        cin>>w;
        int n;
        cin>>n;
        char x[n];
        int b[n];
        for(int i = 0;i<n;i++)
            cin>>x[i];
        for(int i = 0;i<n;i++)
            cin>>b[i];
        Solution ob;
        cout << ob.maxSum(w,x,b,n) << endl;
    }
    return 0; 
}
// } Driver Code Ends