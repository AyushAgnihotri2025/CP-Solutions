//{ Driver Code Starts
// initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    struct suffix {
        int index;   
        int rank[2]; 

    };

    static int cmp(struct suffix a, struct suffix b) {
        return (a.rank[0] == b.rank[0]) ? (a.rank[1] < b.rank[1] ? 1 : 0)
                                        : (a.rank[0] < b.rank[0] ? 1 : 0);
    }

    vector<int> buildSuffixArray(string txt, int n) {
        struct suffix suffixes[n];
        for (int i = 0; i < n; i++) {
            suffixes[i].index = i;
            suffixes[i].rank[0] = txt[i] - 'a';
            suffixes[i].rank[1] = ((i + 1) < n) ? (txt[i + 1] - 'a') : -1;
        }
        sort(suffixes, suffixes + n, cmp);
        int ind[n]; 
        for (int k = 4; k < 2 * n; k = k * 2) {
            int rank = 0;
            int prev_rank = suffixes[0].rank[0];
            suffixes[0].rank[0] = rank;
            ind[suffixes[0].index] = 0;
            for (int i = 1; i < n; i++) {

                if (suffixes[i].rank[0] == prev_rank &&
                    suffixes[i].rank[1] == suffixes[i - 1].rank[1]) {
                    prev_rank = suffixes[i].rank[0];
                    suffixes[i].rank[0] = rank;
                } else {
                    prev_rank = suffixes[i].rank[0];
                    suffixes[i].rank[0] = ++rank;
                }
                ind[suffixes[i].index] = i;
            }
            for (int i = 0; i < n; i++) {
                int nextindex = suffixes[i].index + k / 2;
                suffixes[i].rank[1] =
                    (nextindex < n) ? suffixes[ind[nextindex]].rank[0] : -1;
            }
            sort(suffixes, suffixes + n, cmp);
        }
        vector<int> suffixArr;
        for (int i = 0; i < n; i++) suffixArr.push_back(suffixes[i].index);
        return suffixArr;
    }

    vector<int> kasai(string txt, vector<int> suffixArr) {
        int n = suffixArr.size();
        vector<int> lcp(n, 0);
        vector<int> invSuff(n, 0);
        for (int i = 0; i < n; i++) invSuff[suffixArr[i]] = i;
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (invSuff[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = suffixArr[invSuff[i] + 1];
            while (i + k < n && j + k < n && txt[i + k] == txt[j + k]) k++;
            lcp[invSuff[i]] = k; 
            if (k > 0) k--;
        }
        return lcp;
    }

    int sumOfFirstN(int N) { return (N * (N + 1)) / 2; }

    char PrintKthCharacter(string S, int K) {
        // code here
        int n = S.length();
        vector<int> suffixArr = buildSuffixArray(S, n);
        vector<int> lcp = kasai(S, suffixArr);
        for (int i = 0; i < lcp.size(); i++) {
            int charToSkip = sumOfFirstN(n - suffixArr[i]) - sumOfFirstN(lcp[i]);
            if (K <= charToSkip) {
                for (int j = lcp[i] + 1; j <= (n - suffixArr[i]); j++) {
                    int curSubstringLen = j;
                    if (K <= curSubstringLen) return S[(suffixArr[i] + K - 1)];
                    else K -= curSubstringLen;
                }
                break;
            } else {
                K -= charToSkip;
            }
        }
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin>>t;
    while(t--){
        string S;
        cin >> S;
        int K;
        cin >> K;
    
        Solution ob;
        cout << ob.PrintKthCharacter(S, K) << endl;
    }
}
// } Driver Code Ends