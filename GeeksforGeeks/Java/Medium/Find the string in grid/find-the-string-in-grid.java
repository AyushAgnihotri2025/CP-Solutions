//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s1 = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s1[0]);
            int m = Integer.parseInt(s1[1]);
            char[][] grid = new char[n][m];
            for(int i = 0; i < n; i++){
                String S = br.readLine().trim();
                for(int j = 0; j < m; j++){
                    grid[i][j] = S.charAt(j);
                }
            }
            String word = br.readLine().trim();
            Solution obj = new Solution();
            int[][] ans = obj.searchWord(grid, word);
            for(int i = 0; i < ans.length; i++){
                for(int j = 0; j < ans[i].length; j++){
                    System.out.print(ans[i][j] + " ");
                }
                System.out.println();
            }
            if(ans.length==0)
            {
                System.out.println("-1");
            }

        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    public int[][] searchWord(char[][] grid, String word)
    {
        // Code here
        int row = grid.length;
		int col = grid[0].length;
		int count = 0;
		ArrayList<int[]> arr = new ArrayList<>();
		for(int i=0;i<row;i++) {
			for(int j=0;j<col;j++) {
				boolean ans = false;
				if(grid[i][j] == word.charAt(0)) {
					ans = 	solve(grid,word,i,j,row,col,0,"R") ||
							 solve(grid,word,i,j,row,col,0,"L")||
							solve(grid,word,i,j,row,col,0,"U")||
							solve(grid,word,i,j,row,col,0,"D")||
							 solve(grid,word,i,j,row,col,0,"UR")||
							 solve(grid,word,i,j,row,col,0,"UL")||
							solve(grid,word,i,j,row,col,0,"DR")||
							solve(grid,word,i,j,row,col,0,"DL");
							
				}
				if(ans == true) {
					arr.add(new int[] {i,j});
				}
			
			}
		}
		return arr.toArray(new int[arr.size()][]);
    }

    private static boolean solve(char[][] grid, String word, int i, int j, int row, int col, int curr, 
			String side) {
		
		if(i<0 || j<0 || i>=row || j>=col || grid[i][j] != word.charAt(curr)) {
			return false;
		}
		if(curr == word.length()-1) {
			return true;
		}
		boolean op = false;
		if(side=="R") {
			op = solve(grid, word, i, j+1, row, col, curr+1, side);//right
		}else if(side=="L") {
			op = solve(grid, word, i, j-1, row, col, curr+1, side);//left
		}else if(side=="U") {
			op = solve(grid, word, i-1, j, row, col, curr+1, side);//up
		}else if(side=="D") {
			op = solve(grid, word, i+1, j, row, col, curr+1, side);//down
		}else if(side=="UR") {
			op = solve(grid, word, i-1, j+1, row, col, curr+1, side);//up-right
		}else if(side=="UL") {
			op = solve(grid, word, i-1, j-1, row, col, curr+1, side);//up-left
		}else if(side=="DR") {
			op = solve(grid, word, i+1, j+1, row, col, curr+1, side);//down-right
		}else if(side=="DL"){
			op = solve(grid, word, i+1, j-1, row, col, curr+1, side);//down-left
		}
		
		return op;
    }
}