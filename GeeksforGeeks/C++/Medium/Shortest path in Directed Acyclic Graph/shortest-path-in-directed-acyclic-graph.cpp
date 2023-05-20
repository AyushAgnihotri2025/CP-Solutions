//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
     vector<int> shortestPath(int N,int M, vector<vector<int>>& edges){
        // code here
        vector<pair<int, int>> adj[N];
        for(auto it : edges){
            adj[it[0]].push_back(make_pair(it[1], it[2]));
        }
        vector<int> dist(N, INT_MAX);
        dist[0] = 0;
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));
        while(!q.empty()){
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int dist_of_u = curr.second;
            for(auto it : adj[u])
            {
                int v = it.first;
                int dist_u_to_v = it.second;
                if((dist_u_to_v + dist_of_u) < dist[v]){
                    dist[v] = dist_u_to_v + dist_of_u;
                    q.push(make_pair(v, dist[v]));
                }
            }
        }
        for(int i = 0; i < N; i++){
            if(dist[i] == INT_MAX) dist[i] = -1;
        }
        return dist;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> edges;
        for(int i=0; i<m; ++i){
            vector<int> temp;
            for(int j=0; j<3; ++j){
                int x; cin>>x;
                temp.push_back(x);
            }
            edges.push_back(temp);
        }
        Solution obj;
        vector<int> res = obj.shortestPath(n, m, edges);
        for (auto x : res) {
            cout << x << " ";
        }
        cout << "\n";
    }
}

// } Driver Code Ends