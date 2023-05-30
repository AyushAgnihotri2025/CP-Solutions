//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    int minimumCost(vector<vector<int>>& flights, int n, int k) {
        // code here
        vector<pair<int,int>> graph[n+5];
        for(auto x:flights){
            graph[x[0]].push_back({x[1],x[2]});
        }
        vector<int> cost(n+5,1e9);
        cost[k]=0;
        queue<int> q;
        q.push(k);
        while(q.size()){
            int src=q.front();
            q.pop();
            for(auto dest:graph[src]){
                if(cost[dest.first]>cost[src]+dest.second){
                    q.push(dest.first);
                    cost[dest.first]=cost[src]+dest.second;
                }
            }
        }
        int ans=0;
        for(int i=1;i<=n;i++){
            ans=max(ans,cost[i]);
        }
        return ans==1e9?-1:ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        int size;
        cin >> size;
        vector<vector<int>> flights(size,vector<int>(3));
        for (int i = 0; i < size; i++) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            flights[i]=temp;
        }

        Solution ob;
        cout << ob.minimumCost(flights, n, k) << "\n";
    }
}

// } Driver Code Ends