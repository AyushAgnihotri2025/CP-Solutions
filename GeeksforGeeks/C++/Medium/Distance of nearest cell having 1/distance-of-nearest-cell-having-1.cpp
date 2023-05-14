//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution 
{
    public:
    //Function to find distance of nearest 1 in the grid for each cell.
	vector<vector<int>>nearest(vector<vector<int>>grid)
	{
	    // Code here
	    int n = grid.size();
	    int m = grid[0].size();
	    vector<vector<int>> mat = grid;
	    vector<vector<int>> ans(n,vector<int> (m,0));
	    queue<pair<int,int>> pq;
	    for(int i=0;i<n;i++){
	        for(int j=0;j<m;j++){
	            if(grid[i][j]==1){
	                pq.push(make_pair(i,j));
	            }
	        }
	    }
	    int delrow[]={-1,1,0,0};
	    int delcol[]={0,0,-1,1};
	    int dis=0;
	    while(!pq.empty()){
	        int len = pq.size();
	        while(len--){
	            int row = pq.front().first;
	            int col = pq.front().second;
	            pq.pop();
	            ans[row][col]=dis;
	            for(int i=0;i<4;i++){
	                int nrow = row + delrow[i];
	                int ncol = col + delcol[i];
	                if(nrow>=0&&nrow<n&&ncol>=0&&ncol<m&&mat[nrow][ncol]==0){
	                    pq.push(make_pair(nrow,ncol));
	                    mat[nrow][ncol]=1;
	                }
	            }
	        }
	        dis++;
	    }
	    return ans;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>grid(n, vector<int>(m, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		vector<vector<int>> ans = obj.nearest(grid);
		for(auto i: ans){
			for(auto j: i){
				cout << j << " ";
			}
			cout << "\n";
		}
	}
	return 0;
}
// } Driver Code Ends