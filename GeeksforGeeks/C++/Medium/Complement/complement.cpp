//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution{
public:
    vector<int> findRange(string str, int n) {
        // code here
        int count = 0;
        int maxCount = 0;
        int l = -1, r = -1;
        int L = -1, R = -1;
        int i = 0;
        while(i<n) {
            if(l == -1 && str[i] == '0') l = i;
            if(str[i] == '0') count++;
            else count--;
            
            if(count >= 0) {
                if(maxCount < count) {
                    L = l;
                    R = r = i;
                    maxCount = count;
                }
                i++;
            }
            else {
                while(i < n && str[i] != '0')
                    i++;
                if(i != n) {
                    l = r = i;
                }
                count = 0;
            }
        }
        
        vector<int> ans;
        if(L == -1) {
            ans.push_back(-1);
        }
        else {
            ans.push_back(L+1);
            ans.push_back(R+1);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        Solution ob;
        auto ans = ob.findRange(s, n);

        if (ans.size() == 1) {
            cout << ans[0] << "\n";
        } else {
            cout << ans[0] << " " << ans[1] << "\n";
        }
    }
    return 0;
}
// } Driver Code Ends