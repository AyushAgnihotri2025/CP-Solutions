class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int i, j, k, n = piles.size();
        int s=0, p[n], dp[n][n+1];
        memset(dp, 0, sizeof(dp));
        for(i=0;i<n;i++){
            s += piles[i];
            p[i] = s;
            dp[n-1][i+1] = piles[n-1];
        }
        if(n<3)
            return s;
        for(i=n-2;i>=0;i--){
            int start = 0;
            if(i!=0)
                start = p[i-1];
            for(j=1;j<=n;j++){
                if(i+j >= n){
                    dp[i][j] = p[n-1] - start;
                    continue;
                }
                for(k=1;k<=j;k++){
                    if(i+k-1 >= n-1){ 
                        dp[i][j] = p[n-1] - start;
                        break;
                    }
                    int imm = p[i+k-1] - start;
                    int mxjmp = max(2*k, j);
					int later_picked = 0;
                    if(mxjmp > n)
                        mxjmp = n;
                    later_picked = p[n-1] - p[i+k-1] - dp[i+k][mxjmp];
                    dp[i][j] = max(dp[i][j], imm + later_picked);
                }
            }
        }
        return dp[0][2];
    }
};