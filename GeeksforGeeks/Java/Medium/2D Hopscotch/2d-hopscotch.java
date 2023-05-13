//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String arr[] = in.readLine().trim().split("\\s+");
            int n = Integer.parseInt(arr[0]);
            int m = Integer.parseInt(arr[1]);
            int mat[][] = new int[n][m];
            for(int i = 0;i < n;i++){
                String a[] = in.readLine().trim().split("\\s+");
                for(int j = 0;j < m;j++)
                    mat[i][j] = Integer.parseInt(a[j]);
            }
            String a1[] = in.readLine().trim().split("\\s+");
            int ty = Integer.parseInt(a1[0]);
            int i = Integer.parseInt(a1[1]);
            int j = Integer.parseInt(a1[2]);
            
            Solution ob = new Solution();
            System.out.println(ob.hopscotch(n, m, mat, ty, i, j));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static int hopscotch(int n, int m, int mat[][], int ty, int i, int j) 
    {
        // code here
        Queue<int[]> q=new LinkedList<>();
        q.add(new int[]{i,j,0});
        int ans=0;
        while(!q.isEmpty()){
            int[] v=q.poll();
            int a=v[0], b=v[1], step=v[2];
            if(step==ty+1)
                ans+=mat[a][b];
            else{
                int[] dir=new int[]{0,-1,0,1,0};
                for(int it=0;it<4;it++)
                    add(mat,a+dir[it],b+dir[it+1],q,step+1);
                int up=(b%2==1)?1:-1;
                add(mat,a+up,b-1,q,step+1);
                add(mat,a+up,b+1,q,step+1);
            }
            mat[a][b]=0;
        }
        return ans;
    }
    
    static void add(int mat[][], int i, int j,Queue<int[]> q,int step){
        if(i<0||j<0||i>=mat.length||j>=mat[0].length)return;
            q.add(new int[]{i,j,step});
    }
}