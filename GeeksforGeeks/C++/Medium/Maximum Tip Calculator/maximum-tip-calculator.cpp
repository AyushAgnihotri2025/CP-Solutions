//{ Driver Code Starts
//Initial Template for C++



#include <bits/stdc++.h>

using namespace std;



// } Driver Code Ends
//User function Template for C++

class Solution{
  public:
    static bool compartor(pair<int, int> a, pair<int, int> b) {
        return abs(a.first) > abs(b.first);
    }

    long long maxTip(int a[], int b[], int n, int x, int y) {
        // code here
        vector<pair<int, int>> mp;
        vector<int> visited(n,0);
        
        long long sum=0;
        for(int i=0;i<n;i++)
            mp.push_back({a[i]-b[i], i});
            
        sort(mp.begin(), mp.end(), compartor);
        
        for(int i=0;i<n;i++) {
            auto ele = mp[i];
            if(ele.first == 0)
                break;
                
            if(ele.first > 0 && x > 0 || y <= 0 && x > 0) {
                visited[ele.second] = 1;
                x--;
            } else {
                visited[ele.second] = 0;
                y--;
            }
        }
        
        long long tmp;
        for(int i=0;i<n;i++) {
            if(visited[i])
                tmp = a[i];
            else
                tmp = b[i];
                
            sum += tmp;
        }
        
        return sum;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x, y;
        cin >> n >> x >> y;
        int a[n], b[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> b[i];
        }
        Solution obj;
        auto ans = obj.maxTip(a, b, n, x, y);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends