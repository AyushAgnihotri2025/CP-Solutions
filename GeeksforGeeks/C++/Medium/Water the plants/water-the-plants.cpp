//{ Driver Code Starts
// driver code

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    int min_sprinklers(int gallery[], int n)
    {
        // code here
        vector<pair<int, int>> v;
        for (int i = 0; i < n; i++) {
            if (gallery[i] == -1)
                continue;
            v.push_back({
                max(0, i - gallery[i]),
                min(n - 1, i + gallery[i])
            });
        }
        sort(v.begin(), v.end());
        int start = 0, i = 0, ans = 0;
        while (start < n) {
            int mx = INT_MIN;
            while (i < v.size()) {
                if (v[i].first > start)
                    break;
                mx = max(mx, v[i].second);
                i++;
            }
            if (mx < start)
                return -1;
            ans++;
            start = mx + 1;
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        int gallery[n];
        for(int i=0; i<n; i++)
            cin>> gallery[i];
        Solution obj;
        cout<< obj.min_sprinklers(gallery,n) << endl;
    }
	return 1;
}

// } Driver Code Ends