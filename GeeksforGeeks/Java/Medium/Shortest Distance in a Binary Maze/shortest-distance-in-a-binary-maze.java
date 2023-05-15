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
            int[] source = new int[2];
            for (int i = 0; i < 2; i++) {
                int x = sc.nextInt();
                source[i] = x;
            }
            int[] dest = new int[2];
            for (int i = 0; i < 2; i++) {
                int x = sc.nextInt();
                dest[i] = x;
            }
            Solution ob = new Solution();
            int ans = ob.shortestPath(grid, source, dest);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int shortestPath(int[][] grid, int[] source, int[] destination) {
        // Your code here
        int n = grid.length, m = grid[0].length;
        if (source[0] == destination[0] && source[1] == destination[1]) return 0;
        int memo[][] = new int[n][m];
        for (int me[]: memo) Arrays.fill(me, 2501);
        memo[source[0]][source[1]] = 0;
        int dir[] = {
            0,
            -1,
            0,
            1,
            0
        };
        Queue < int[] > q = new LinkedList < > ();
        q.add(new int[] {
            0,
            source[0],
            source[1]
        });
        while (!q.isEmpty()) {
            int par[] = q.poll();
            int pi = par[1];
            int pj = par[2];
            int pd = par[0];
            for (int k = 0; k < 4; k++) {
                int nr = pi + dir[k], nc = pj + dir[k + 1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 1 && pd + 1 < memo[nr][nc]) {
                    memo[nr][nc] = pd + 1;
                    q.add(new int[] {
                        pd + 1, nr, nc
                    });
                    if (nr == destination[0] && nc == destination[1]) return pd + 1;
                }
            }

        }
        return -1;
    }
}
