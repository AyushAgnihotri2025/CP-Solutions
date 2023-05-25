//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    void dfs(int r,int c,vector<vector<int>>&mat,vector<vector<int>>&vis,int n,int m){
        vis[r][c] = 1;
        int dx[4] = {-1,1,0,0}, dy[4] = {0,0,-1,1};
        for(int i=0;i<4;i++) {
            int nx=r+dx[i], ny=c+dy[i];
            if(nx>=0 and ny>=0 and nx<n and ny<m and mat[nx][ny]==1 and !vis[nx][ny]) dfs(nx,ny,mat,vis,n,m);
        }
    }

    vector<int> numOfIslands(int n, int m, vector<vector<int>> &operators) {
        // code here
        vector<vector<int>> matrix(n,vector<int>(m));
        vector<int>ans;
        for(auto op: operators) {
            int r = op[0], c = op[1];
            matrix[r][c] = 1;
            int count = 0;
            vector<vector<int>> vis(n,vector<int>(m));
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++) {
                    if(matrix[i][j] == 1 and !vis[i][j]) {
                        count++;
                        dfs(i,j,matrix,vis,n,m);
                    }
                }
            }
            ans.push_back(count);
        }
        
        return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n,m,k; cin>>n>>m>>k;
        vector<vector<int>> a;
        
        for(int i=0; i<k; i++){
            vector<int> temp;
            for(int j=0; j<2; j++){
                int x; cin>>x;
                temp.push_back(x);
            }
            a.push_back(temp);
        }
    
        Solution obj;
        vector<int> res = obj.numOfIslands(n,m,a);
        
        for(auto x : res)cout<<x<<" ";
        cout<<"\n";
    }
}

// } Driver Code Ends