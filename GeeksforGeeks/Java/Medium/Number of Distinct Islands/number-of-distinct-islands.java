//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] grid = new int[n][m];

            for (int i = 0; i < n; i++) {

                for (int j = 0; j < m; j++) {
                    grid[i][j] = sc.nextInt();
                }
            }

            Solution ob = new Solution();
            int ans = ob.countDistinctIslands(grid);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int dr[]={-1,0,0,1};
    int dc[]={0,-1,1,0};

    int countDistinctIslands(int[][] grid) {
        // Your Code here
        HashSet<List<Integer>> set=new HashSet<>();
        boolean vis[][]=new boolean[grid.length][grid[0].length];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(!vis[i][j] && grid[i][j] == 1){
                    List<Integer> list=new ArrayList<>();
                    DFS( i, j, vis, list, grid, i, j);
                    set.add(list);
                }
            }
        }
        return set.size();
    }

    private void DFS(int r , int c ,boolean vis[][] ,List<Integer> ans, int grid[][] , int mrow , int mcol){
        vis[r][c]=true;
        ans.add(r-mrow);
        ans.add(c-mcol);
        for(int i=0;i<4;i++){
            int nr=dr[i]+r;
            int nc=dc[i]+c;
            if( nr>=0 && nr<grid.length && nc>=0 && nc<grid[0].length && !vis[nr][nc]  && grid[nr][nc] == 1 ){
                DFS( nr, nc, vis, ans, grid, mrow, mcol);
            }
        }
    }
}
