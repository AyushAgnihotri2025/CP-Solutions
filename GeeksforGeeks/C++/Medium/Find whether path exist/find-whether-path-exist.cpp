//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
    public:
    //Function to find whether a path exists from the source to destination.
    bool is_Possible(vector<vector<int>>& grid) 
    {
        //code here
        vector<vector<int>> dir = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        queue<pair<int,int>> q;
        for(int i = 0; i < grid.size(); i++)
            for(int j = 0; j < grid[0].size(); j++) 
                if(grid[i][j] == 1) {
                    q.push({i,j});
                    break;
                }
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> v(m, vector<int>(n,0));
        while(q.size()) {
            auto p = q.front(); q.pop();
            for(auto d: dir) {
                int x=d[0]+p.first, y= d[1]+p.second;
                if(x >=m || x < 0|| y >= n || y < 0 || grid[x][y]==0 || v[x][y]) 
                    continue;
                if(grid[x][y] == 2) return 1;
                q.push({x, y});
                v[x][y] = 1;
            }
        }
        return 0;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>>grid(n, vector<int>(n, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		bool ans = obj.is_Possible(grid);
		cout << ((ans) ? "1\n" : "0\n");
	}
	return 0;
}
// } Driver Code Ends