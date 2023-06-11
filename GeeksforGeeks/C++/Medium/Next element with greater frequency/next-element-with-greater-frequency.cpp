//{ Driver Code Starts
#include <bits/stdc++.h>
#define N 10000
using namespace std;


// } Driver Code Ends
class Solution{
public:
    vector<int> print_next_greater_freq(int arr[],int n)
    {
        // code here
        unordered_map<int,int>m;
        for(int i=0;i<n;i++){
            m[arr[i]]++;
        }
        stack<pair<int,int>>st;
        vector<int> ans;
        ans.push_back(-1); // for last element
        int i =n-1;
        while(i>=0){
            if(st.empty()){
                st.push({arr[i], m[arr[i]]});
            }
            else{
                if(st.top().second>m[arr[i]]){
                    ans.push_back(st.top().first);
                }
                else{
                     while(!st.empty() && st.top().second <= m[arr[i]]){
                        st.pop();
                    }
                    if(st.empty()){
                         ans.push_back(-1);
                    }
                    else{
                        ans.push_back(st.top().first);
                    }
                }
                 st.push({arr[i], m[arr[i]]});
            }
            i--;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};


//{ Driver Code Starts.

int main()
{
    int arr[N];
    
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        for(int i=0; i<n; i++)
            cin>>arr[i];
        
        Solution ob;
        vector<int> ans=ob.print_next_greater_freq(arr,n);
        for(auto x:ans){
            cout<<x<<" ";
        }
        cout << endl;
    }
	return 1;
}

// } Driver Code Ends