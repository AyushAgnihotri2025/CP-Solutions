//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    bool canPair(vector<int> nums, int k) {
        // Code here.
        if(nums.size()%2!=0)    return false;
        unordered_map<int, int> mp;
        for(auto val: nums)
            mp[val%k]++;
        
        for(auto it: mp){
            int val1 = it.first;
            int val2 = abs(k-it.first);
            
            if(val1==0 and mp[val1]%2==0)
                continue;
            
            if(mp.find(val2)==mp.end()) return false;
            if(mp[val1]!=mp[val2])  return false;
        }
        return true;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, k;
        cin >> n >> k;
        vector<int> nums(n);
        for (int i = 0; i < nums.size(); i++) cin >> nums[i];
        Solution ob;
        bool ans = ob.canPair(nums, k);
        if (ans)
            cout << "True\n";
        else
            cout << "False\n";
    }
    return 0;
}
// } Driver Code Ends