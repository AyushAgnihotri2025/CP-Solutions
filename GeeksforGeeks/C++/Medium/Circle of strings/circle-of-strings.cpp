//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution
{
    public:
        void dfs(int node, vector<int>adj[], vector<int>&vis) {
            vis[node] = 1;
            for(auto i: adj[node]) {
                if(!vis[i]) dfs(i,adj,vis);
            }
        }
    
        bool detectCycle(int src, vector<int>adj[], vector<int>&mark) {
            vector<int>vis(26);
            dfs(src,adj,vis);
            for(int i=0;i<26;i++) {
                if(!vis[i] and mark[i] == 1) return 0;
            }
            return 1;
        }
    
        int isCircle(int N, vector<string> A)
        {
            // code here
            vector<int> mark(26), adj[26];
            int in[26] = {0}, out[26] = {0};
            for(auto i: A) {
                int u = i.front() - 'a', v = i.back() - 'a';
                adj[u].push_back(v);
                mark[u] = mark[v] = 1;
                in[v]++;
                out[u]++;
            }
            
            for(int i=0;i<26;i++) if(in[i] != out[i]) return 0;
    
            return detectCycle(A[0].front() - 'a', adj, mark);
        }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        vector<string> A;
        string s;
        
        for(int i = 0;i < N; i++)
        {
            cin>>s;
            A.push_back(s);
        }
        
        Solution ob;
        cout<<ob.isCircle(N, A)<<endl;
    }
    return 0;
}
// } Driver Code Ends