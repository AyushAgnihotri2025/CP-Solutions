//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int countPaths(int n, vector<vector<int>>& roads) {
        // code here
        vector<pair<long long,long long>>adj[n];
        for(auto it:roads){
            adj[it[0]].push_back({it[1],it[2]});
            adj[it[1]].push_back({it[0],it[2]});
        }
        vector<long long>dist(n,1e15);
        vector<long long>ways(n,0);
        set<pair<long long,long long>>s;
        dist[0]=0;
        ways[0]=1;
        s.insert({0,0});
        int mod=(int)(1e9+7);
        while(!s.empty()){
            auto ptr=*(s.begin());
            long long cost=ptr.first;
            long long node=ptr.second;
            s.erase(ptr);
            
            for(auto it:adj[node]){
                long long child=it.first;
                long long wt=it.second;
                
                if(cost+wt<dist[child]){
                    dist[child]=cost+wt;
                    s.insert({wt+cost,child});
                    ways[child]=ways[node];
                }
                
                else if(cost+wt==dist[child]){
                    ways[child]=(ways[child]+ways[node])%mod;
                }
            }
        }
        return ways[n-1]%mod;
    }
};

//{ Driver Code Starts.

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        int u, v;

        vector<vector<int>> adj;

        for (int i = 0; i < m; ++i) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }

        Solution obj;
        cout << obj.countPaths(n, adj) << "\n";
    }

    return 0;
}
// } Driver Code Ends