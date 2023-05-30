//{ Driver Code Starts
// Initial Template for C#

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DriverCode {

class GFG {
    static void Main(string[] args) {
        int testcases; // Taking testcase as input
        testcases = Convert.ToInt32(Console.ReadLine());
        while (testcases-- > 0) // Looping through all testcases
        {
            var ip = Console.ReadLine().Trim().Split(' ');
            int V = int.Parse(ip[0]);
            int E = int.Parse(ip[1]);
            List<List<int>> adj = new List<List<int>>();
            for (int i = 0; i < V; i++) {
                adj.Add(new List<int>());
            }
            for (int i = 0; i < E; i++) {
                ip = Console.ReadLine().Trim().Split(' ');
                int u = int.Parse(ip[0]);
                int v = int.Parse(ip[1]);
                adj[u].Add(v);
                adj[v].Add(u);
            }
            Solution obj = new Solution();
            var res = obj.printGraph(V, adj);
            for (int i = 0; i < res.Count; i++) {
                for (int j = 0; j < res[i].Count - 1; j++) {
                    Console.Write(res[i][j] + "-> ");
                }
                Console.WriteLine(res[i][res[i].Count - 1]);
            }
        }
    }
}
}
// } Driver Code Ends


// User function Template for C#

class Solution {

    // Function to return the adjacency list for each vertex.
  public
    List<List<int>> printGraph(int V, List<List<int>> adj) {
        // Code here
        List<List<int>> ans = new List<List<int>>();
        for (int i = 0; i < V; i++)
        {
            ans.Add(new List<int> { i });
        }
    
        for (int i = 0; i < V; i++)
        {
            for (int j = 0; j < adj[i].Count; j++)
            {
                ans[i].Add(adj[i][j]);
            }
        }
    
        return ans;
    }
}