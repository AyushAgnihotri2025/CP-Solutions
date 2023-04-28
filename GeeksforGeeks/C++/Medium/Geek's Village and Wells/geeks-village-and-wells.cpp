//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    vector<vector<int>> chefAndWells(int n,int m,vector<vector<char>> &c){
        // Code here
        queue<pair<int, int>> q;
        vector<vector<int>> dist(n, vector<int> (m, INT_MAX));
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(c[i][j] == 'W') {
                    q.push({i, j});
                    dist[i][j] = 0;
                }
            }
        }
        int d[] = {0, 1, 0, -1, 0};
        while(!q.empty()) {
            auto cell = q.front();
            int r = cell.first, cc = cell.second;
            q.pop();
            for(int i = 0; i < 4; i++) {
                int R = r + d[i], C = cc + d[i+1];
                if(R >= 0 && R < n && C >= 0 && C < m && c[R][C] != 'N' && dist[R][C] == INT_MAX) {
                    q.push({R, C});
                    dist[R][C] = dist[r][cc] + 1;
                }
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(c[i][j] == 'H') dist[i][j] = dist[i][j] == INT_MAX ? -1 : dist[i][j] * 2;
                else dist[i][j] = 0;
            }
        }
        return dist;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        vector<vector<char>> c(n,vector<char>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>c[i][j];
            }
        }
        Solution ob;
        vector<vector<int>> res=ob.chefAndWells(n,m,c);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cout<<res[i][j]<<" ";
            }
            cout<<endl;
        }
    }
}
// } Driver Code Ends