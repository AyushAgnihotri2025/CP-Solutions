//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
        int minimumEdgeReversal(vector<vector<int>> &edges,int n,int src,int dst)
        {
                   vector<vector<pair<int,int>>> adj(n+1);
                    for(auto it:edges)
                    {
                        adj[it[0]].push_back({0,it[1]});
                        adj[it[1]].push_back({1,it[0]});
                    }
                    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
                    pq.push({0,src});
                    vector<int> dist(n+1,1e5);
                    dist[src] = 0;
                    while(!pq.empty())
                    {
                        pair<int,int> pp = pq.top();
                        pq.pop();
                        int u = pp.second;
                        int cost = pp.first;
                        if(u == dst)
                            return cost;
                        for(auto it:adj[u])
                        {
                            int wt = it.first;
                            int v = it.second;
                            if(dist[v] > dist[u]+wt)
                            {dist[v] = cost+wt;
                            pq.push({cost+wt,v});}
                        }
                    }
                    return -1;   
        }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<vector<int>> edges(m,vector<int> (2));
        for(auto &j:edges)
            for(auto &i:j)
                cin>>i;
        int src,dst;
        cin>>src>>dst;
        Solution s;
        cout<<s.minimumEdgeReversal(edges,n,src,dst)<<endl;
    }
    return 0;
}
// } Driver Code Ends