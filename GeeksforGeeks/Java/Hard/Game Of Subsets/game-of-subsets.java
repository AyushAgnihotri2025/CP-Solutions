//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            Solution ob = new Solution();
            int ans = ob.goodSubsets(a, n);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int mod;
    int[] mp;
    
    public Solution() {
        mod = (int) 1e9 + 7;
        mp = new int[31];
        int[] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        for (int i = 2; i <= 30; ++i) {
            if (i % 4 == 0 || i % 9 == 0 || i == 25) continue;
            int mask = 0;
            for (int j = 0; j < 10; ++j) {
                if (i % prime[j] == 0) mask |= 1 << j;
            }
            mp[i] = mask;
        }
    }
    
    public long pow(int n) {
        long ans = 1, m = 2;
        while (n != 0) {
            if ((n & 1) == 1) ans = (ans * m) % mod;
            m = (m * m) % mod;
            n >>= 1;
        }
        return ans;
    }
    
    public int goodSubsets(int[] arr, int n) {
        // Code here
        int one = 0;
        int[] dp = new int[1024];
        int[] cnt = new int[31];
        dp[0] = 1;
        for (int i : arr) {
            if (i == 1) {
                one++;
            } else if (mp[i] != 0) {
                cnt[i]++;
            }
        }
        for (int i = 0; i < 31; ++i) {
            if (cnt[i] == 0) continue;
            for (int j = 0; j < 1024; ++j) {
                if ((j & mp[i]) != 0) continue;
                dp[j | mp[i]] = (int) ((dp[j | mp[i]] + dp[j] * (long) cnt[i]) % mod);
            }
        }
        long ans = 0;
        for (int i : dp) {
            ans = (ans + i) % mod;
        }
        ans--;
        if (one != 0) {
            ans = (ans * pow(one)) % mod;
        }
        return (int) ans;
    }
};