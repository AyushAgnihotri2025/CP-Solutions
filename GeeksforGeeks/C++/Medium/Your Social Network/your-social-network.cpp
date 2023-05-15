//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    void dfs(vector<vector<int>>& graph, int count, int src, vector<vector<int>>& temp) {
        
        for(auto& x: graph[src]) {
            dfs(graph, count+1, x, temp);
        }
        
        temp.push_back({src, count});
    }

    string socialNetwork(int arr[], int N) {
        // code here
        vector<vector<int>> graph(N+1);
        for(int i = 0 ; i < N-1; ++i) {
            int u = i+2;
            int v = arr[i];
            graph[u].push_back(v);
        }
        vector<vector<int>> temp;
        string ans = "";
        for(int i = 2; i <= N; ++i) {
            dfs(graph, 0, i, temp);
            temp.pop_back();
            for(int j = 0; j < temp.size(); ++j) {
                ans = ans + to_string(i) + " " + to_string(temp[j][0]) + " " + to_string(temp[j][1]) + " "; 
            }
            temp.clear();
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        
        int arr[N-1];
        for(int i=0; i<N-1; i++)
            cin>>arr[i];

        Solution ob;
        cout << ob.socialNetwork(arr,N) << endl;
    }
    return 0;
}
// } Driver Code Ends