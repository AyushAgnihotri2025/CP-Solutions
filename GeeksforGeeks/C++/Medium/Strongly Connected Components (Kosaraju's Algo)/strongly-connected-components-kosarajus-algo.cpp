//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
	public:
	void topo(int i, vector<vector<int>>& adj, vector<int> &vis, stack<int> &st){
	    vis[i]=1;
	    for(auto x: adj[i])
	        if(vis[x]==0)
	            topo(x,adj,vis,st);
	    st.push(i);
	}
	void dfs(int i, vector<int> adj[], vector<int> &vis, vector<int> &ans){
	    vis[i]=1; ans.push_back(i);
	    for(auto x: adj[i])
	        if(vis[x]==0)
	            dfs(x, adj, vis, ans);
	}
	//Function to find number of strongly connected components in the graph.
    int kosaraju(int V, vector<vector<int>>& adj)
    {
        //code here
        vector<vector<int>> ans;
        stack<int> st;
        vector<int> vis(V,0);
        for(int i=0;i<V;i++)
            if(vis[i]==0)
                topo(i, adj, vis, st);
        
        vector<int> tranpose[V];
        for(int i=0;i<V;i++){
            vis[i]=0;
            for(auto x: adj[i]){
                tranpose[x].push_back(i);
            }
        }
        while(st.size()) {
            int node=st.top(); st.pop();
            if(vis[node]==0){
                vector<int> temp;
                dfs(node, tranpose, vis, temp);
                ans.push_back(temp);
            }
        }
        return ans.size();
    }
};

//{ Driver Code Starts.


int main()
{
    
    int t;
    cin >> t;
    while(t--)
    {
    	int V, E;
    	cin >> V >> E;

    	vector<vector<int>> adj(V);

    	for(int i = 0; i < E; i++)
    	{
    		int u, v;
    		cin >> u >> v;
    		adj[u].push_back(v);
    	}

    	Solution obj;
    	cout << obj.kosaraju(V, adj) << "\n";
    }

    return 0;
}


// } Driver Code Ends