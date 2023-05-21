//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
private:
    bool isValid(int n, int k, vector<int>& stalls, int distance){
        int curr = stalls[0];
        int cnt = 1;
        for(int i=1; i<n; i++){
            if(abs(stalls[i] - curr)  >=  distance)
                cnt++, curr = stalls[i];
        }
        
        return cnt >= k;
    }
public:
    int solve(int n, int k, vector<int> &stalls) {
    
        // Write your code here
        int start = 1;
        int end = *max_element(stalls.begin(), stalls.end());
        sort(stalls.begin(), stalls.end());
        
        while(start <= end){
            int mid = start+(end-start)/2;
            if(isValid(n, k, stalls, mid))
                start = mid+1;
            else
                end = mid-1;
        }
        
        return end;
    }
};

//{ Driver Code Starts.

int main() {
    int t = 1;
    cin >> t;

    // freopen ("output_gfg.txt", "w", stdout);

    while (t--) {
        // Input

        int n, k;
        cin >> n >> k;

        vector<int> stalls(n);
        for (int i = 0; i < n; i++) {
            cin >> stalls[i];
        }
        // char ch;
        // cin >> ch;

        Solution obj;
        cout << obj.solve(n, k, stalls) << endl;

        // cout << "~\n";
    }
    // fclose(stdout);

    return 0;
}
// } Driver Code Ends