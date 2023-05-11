//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    // Driver code
    public static void main(String[] args) throws Exception {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] str = br.readLine().trim().split(" ");
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(str[i]);
            }

            ArrayList<Integer> ans = new Solution().findSubarray(a, n);
            for(int i:ans){
                out.print(i+" ");
            }out.println();
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {

    ArrayList<Integer> findSubarray(int a[], int n) {
        // code here
        int sInd = -1, eInd = 0, sum = 0;
        int maxSInd = 0, maxEInd = 0, maxSum = Integer.MIN_VALUE;
        for(int i = 0 ; i < n ; i++){
            int num = a[i];
            if(num > 0){
                sum += num;
                eInd = i;
            }
            else if(num == 0){
                if(maxSum == 0)maxSum = Integer.MIN_VALUE;
                eInd = i;
            }
            else{
                sum = 0;
                sInd = i;
                continue;
            }
            if(sum > maxSum){
                maxSInd = sInd;
                maxEInd = eInd;
                maxSum = sum;
            }
            else if(sum == maxSum){
                if(eInd - sInd > maxEInd - maxSInd){
                    maxSInd = sInd;
                    maxEInd = eInd;
                    maxSum = sum;
                }
            }
        }
        ArrayList<Integer> res = new ArrayList<>();
        for(int i = maxSInd+1 ; i <= maxEInd ; i++){
            res.add(a[i]);
        }
        if(res.isEmpty())res.add(-1);
        return res;
    }
}