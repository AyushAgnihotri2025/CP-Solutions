//{ Driver Code Starts


#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class DSU {
    private:
    vector<int> par;
    vector<int> rank;
    int size;
    
    public:
    DSU(int size) {
        this->size = size;
        for(int i = 0 ; i < size ; ++i) {
            par.push_back(i);
            rank.push_back(1);
        }
    }
    
    int find(int a) {
        
        if(a == par[a])
            return a;
            
        else 
            return par[a] = find(par[a]);
    }
    
    void union_(int a, int b) {
        
        //sanity check
        assert(a < size);
        assert(b < size);
        
        int par_a  = find(a);
        int par_b  = find(b);
        
        if(par_a == par_b)
            return;
            
        if(rank[par_a] > rank[par_b]) {
            par[par_b] = par_a;
            rank[par_a] += rank[par_b];
        }
        
        else {
            par[par_a] = par_b;
            rank[par_b] += rank[par_a];
        }
    }
    
    bool isConnected(int a, int b) {
        assert(a < size);
        assert(b < size);
        
        if(find(a) == find(b))
            return true;
        
        else 
            return false;
    }
};

class Solution {
  public:
    int RevDelMST(int Arr[], int V, int E) {
        // code here
        vector<vector<int>> edges;
        vector<int> degree(V, 0);
        
        for(int i = 0; i < (3*E)-2; i+=3) {
            
            int u = Arr[i];
            int v = Arr[i+1];
            int w = Arr[i+2];
            
            edges.push_back({u,v,w});
        }
        
        sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {return a[2] < b[2];});
        
        int wt = 0;
        
        DSU ds(V);
        
        for(int i = 0 ; i < edges.size(); ++i) {
            
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            
            
            if(!ds.isConnected(u,v)) {
                wt += w;
                ds.union_(u,v);
            }
            
        }
        return wt;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int V,E;
        cin>>V>>E;

        int Arr[3*E];
        for(int i=0; i<3*E; i++)
            cin>>Arr[i];

        Solution ob;
        cout << ob.RevDelMST(Arr,V,E) << endl;
    }
    return 0;
}
// } Driver Code Ends