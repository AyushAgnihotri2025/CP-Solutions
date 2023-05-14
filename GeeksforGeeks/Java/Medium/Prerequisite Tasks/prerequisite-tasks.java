//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
	public static void main(String args[]) throws IOException
	{
	    Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();
		while(t>0)
		{
		    int N = sc.nextInt();
		    int P = sc.nextInt();
		    int prerequisites[][] = new int[P][2];
		    for(int i=0;i<P;i++)
		    {
		        for(int j=0;j<2;j++)
		        {
		            prerequisites[i][j] = sc.nextInt();
		        }
		    }
			Solution ob = new Solution();
			if(ob.isPossible(N,prerequisites))
			{
			    System.out.println("Yes");
			}
			else{
			    System.out.println("No");
			}
			t--;
		}
	}
	
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    public boolean isPossible(int N, int[][] prerequisites)
    {
        // Your Code goes here

        ArrayList <ArrayList<Integer>> graph= new ArrayList <>();    
        int p= prerequisites.length;
        for(int i=0; i<N; i++){
            graph.add(new ArrayList <>());
        }
        int [] indeg = new int [N];
        for(int i=0; i<p; i++){
            int u=prerequisites[i][0];
            int v=prerequisites[i][1];
            graph.get(u).add(v);
            indeg[v]++;
        }
        Queue <Integer> q= new LinkedList <>();
        for(int i=0; i<N; i++){
            if(indeg[i]==0){
                q.add(i);
            }
        }
        int c=0;
        while(!q.isEmpty()){
            int curr=q.poll();
            c++;
            for(int neighbor: graph.get(curr)){
                indeg[neighbor]--;
                if(indeg[neighbor]==0){
                    q.add(neighbor);
                }
            }
        }
        return c==N;
    }
    
}