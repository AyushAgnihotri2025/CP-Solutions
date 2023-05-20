//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    bool isStraightHand(int N, int groupSize, vector<int> &hand) {
        // code here
        if (N % groupSize) {
            return false;
        }
        sort(hand.begin(), hand.end());
        int i = 0;
        while (i < hand.size()) {
            int j = 0;
            while (j < groupSize - 1) {
                int dist = abs(hand[i + j] - hand[i + j + 1]);
                if (dist > 1) return false;
                j++;
            }
            i += groupSize;
        }
        return true;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, groupSize;
        cin >> N >> groupSize;

        vector<int> hand(N);
        for (int i = 0; i < N; i++) cin >> hand[i];

        Solution obj;
        int ans = obj.isStraightHand(N, groupSize, hand);
        if (ans)
            cout << "True" << endl;
        else
            cout << "False" << endl;
    }
    return 0;
}
// } Driver Code Ends