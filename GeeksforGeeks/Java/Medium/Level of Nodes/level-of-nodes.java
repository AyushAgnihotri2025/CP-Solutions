//{ Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class DriverClass
{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            ArrayList<ArrayList<Integer>> list = new ArrayList<>();
            int V = sc.nextInt();
            int E = sc.nextInt();
            for(int i = 0; i < V+1; i++)
                list.add(i, new ArrayList<Integer>());
            for(int i = 0; i < E; i++)
            {
                int u = sc.nextInt();
                int v = sc.nextInt();
                list.get(u).add(v);
                list.get(v).add(u);
            }
            int X = sc.nextInt();
            
            Solution ob = new Solution();
            
            System.out.println(ob.nodeLevel(V,list,X));
        }
    }
}
// } Driver Code Ends


/*Complete the function below*/

class Solution
{
    //Function to find the level of node X.
    int nodeLevel(int V, ArrayList<ArrayList<Integer>> adj, int X)
    {
        // code here
        if(X >= V) {
            return -1;
        }
        boolean[] visited = new boolean[V];
        int[] level = new int[V];
        Queue<Integer> q = new LinkedList<>();
        visited[0] = true;
        q.add(0);
        level[0] = 0;
        while(!q.isEmpty()) {
            int u = q.remove();
            for(int v: adj.get(u)) {
                if(visited[v] == false) {
                    level[v] = level[u] + 1;
                    visited[v] = true;
                    q.add(v);
                }
            }
        }
       return level[X];
    }
}