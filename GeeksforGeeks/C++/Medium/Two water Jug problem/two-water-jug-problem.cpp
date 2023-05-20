//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	int minSteps(int m, int n, int d)
	{
	    // Code here
	    int ans = 0;
	    queue<pair<int, int>> q;
	    vector<vector<int>> vis(m+1, vector<int>(n+1, 0));
	    q.push({0, 0});
	    vis[0][0] = 1;
	    while(!q.empty()){
	        int sz = q.size();
	        for(int i = 0; i < sz; i++){
	            auto it = q.front();
	            q.pop();
	            int x = it.first;
	            int y = it.second;
	            if(x == d || y == d) return ans;
	            if(!vis[x][n]){
	                vis[x][n] = 1;
	                q.push({x, n});
	            }
	            if(!vis[m][y]){
	                vis[m][y] = 1;
	                q.push({m, y});
	            }
	            if(!vis[x][0]){
	                vis[x][0] = 1;
	                q.push({x, 0});
	            }
	            if(!vis[0][y]){
	                vis[0][y] = 1;
	                q.push({0, y});
	            }
	            if(x+y<=m && !vis[x+y][0]){
	                vis[x+y][0] = 1;
	                q.push({x+y, 0});
	            }
	            if(x+y<=n && !vis[0][x+y]){
	                vis[0][x+y] = 1;
	                q.push({0, x+y});
	            }
	            if(x+y>m && !vis[m][x+y-m]){
	                vis[m][x+y-m] = 1;
	                q.push({m, x+y-m});
	            }
	            if(x+y>n && !vis[x+y-n][n]){
	                vis[x+y-n][n] = 1;
	                q.push({x+y-n, n});
	            }
	        }
	        ans++;
	    }
	    return -1;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m, d;
		cin >> m >> n >> d;
		Solution ob;
		int ans = ob.minSteps(m, n, d);
		cout << ans <<"\n";
	}  
	return 0;
}
// } Driver Code Ends