class Solution {
public:
    const int mod = 1e9+7;
    long dfs(vector<vector<long>>& dp, vector<vector<int>>& cnt, string& target, int i, int j, int n, int m) {
        if (j == m) return 1;
        if (n - i < m - j) return 0;
        if (dp[i][j] != -1) return dp[i][j];
        
        long val = cnt[i][target[j] - 'a'] * dfs(dp, cnt, target, i + 1, j + 1, n, m);
        val += dfs(dp, cnt, target, i + 1, j, n, m);
        val %= mod;
        return dp[i][j] = val;;
    }
    int numWays(vector<string>& words, string target) {
        int n = words[0].length();
        vector<vector<int>> cnt(n, vector<int>(26, 0));
        for (const auto& s: words) {
            for (int i = 0; i < n; i++) {
                cnt[i][s[i]-'a']++;
            }
        }
        
        int m = target.length();
        vector<vector<long>> dp(n, vector<long>(m, -1));
        return dfs(dp, cnt, target, 0, 0, n, m);
    }
};