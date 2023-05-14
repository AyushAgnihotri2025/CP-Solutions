//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int minThrow(int N, int arr[]){
        // code here
        vector<int>a(31,0);
        for(int i=1;i<31;i++) a[i] = i;
        
        for(int i =0;i<2*N;i+=2)
            a[arr[i]] = arr[i+1];
        
        vector<int> vis(31,0);
        queue<pair<int,int>>q;
        
        q.push({1,0});
        vis[1] = 1;
        
        while(!q.empty()){
            int curr = q.front().first;
            int step = q.front().second;
            q.pop();
            for(int i=1;i<=6;i++){
                int nx = curr+i;
                if(nx<31 && !vis[a[nx]]){
                    vis[a[nx]] = 1;
                    q.push({a[nx],step+1});
                    if(a[nx]==30) return step+1;
                }
            }
        }
        return -1;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[2*N];
        for(int i = 0;i < 2*N;i++)
            cin>>arr[i];
        
        Solution ob;
        cout<<ob.minThrow(N, arr)<<"\n";
    }
    return 0;
}
// } Driver Code Ends