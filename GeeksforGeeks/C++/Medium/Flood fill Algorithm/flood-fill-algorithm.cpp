//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
    void dfs(vector<vector<int>> &mat,vector<vector<int>> image, int sr, int sc, int newColor, int col){
        mat[sr][sc] = newColor;
        int row = mat.size();
        int column = mat[0].size();
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        for(int i=0; i<4; i++){
            int r = sr + dx[i];
            int c = sc + dy[i];
            if(r>=0&&r<row&&c>=0&&c<column&&mat[r][c]==col&&image[r][c]!=newColor){
                dfs(mat,image, r, c, newColor, col);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        // Code here 
        vector<vector<int>> mat = image;
        int col = mat[sr][sc];
        dfs(mat, image, sr, sc, newColor, col);
        return mat;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>image(n, vector<int>(m,0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
				cin >> image[i][j];
		}
		int sr, sc, newColor;
		cin >> sr >> sc >> newColor;
		Solution obj;
		vector<vector<int>> ans = obj.floodFill(image, sr, sc, newColor);
		for(auto i: ans){
			for(auto j: i)
				cout << j << " ";
			cout << "\n";
		}
	}
	return 0;
}
// } Driver Code Ends