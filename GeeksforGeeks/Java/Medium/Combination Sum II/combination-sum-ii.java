//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter ot = new PrintWriter(System.out);
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
		    String s[] = br.readLine().trim().split(" ");
			int n = Integer.parseInt(s[0]);
			int k = Integer.parseInt(s[1]);
			int a[] = new int[n];
			s = br.readLine().trim().split(" ");
			for(int i = 0; i < n; i++)
				a[i] = Integer.parseInt(s[i]);
			List<List<Integer>> ans = new Solution().CombinationSum2(a, n, k);
			for(List<Integer> list : ans){
				for(int x : list)
					ot.print(x + " ");
				ot.println();
			}
			if(ans.size() == 0)
			    ot.println();
		}
        ot.close();
	}
}
// } Driver Code Ends


//User function Template for Java

class Solution{
	public int sum(List<Integer> combination) {
        int s = 0;
        for(int ele:combination)
        {
            s += ele;
        }
        return s;
    }

    public void solve(int a[],int index,List<Integer> combination,List<List<Integer>> ans,int k) {
        if(k == 0)
        {
            ans.add(new ArrayList<>(combination));
            return;
        }
        if(k < 0)
        {
            return;
        }
        if(index >= a.length)
        {
            return;
        }
        int prev_ele = -1;
        for(int i=index;i<a.length;i++)
        {
            if(a[i]==prev_ele)
                continue;
            combination.add(a[i]);
            solve(a,i+1,combination,ans,k-a[i]);
            combination.remove(combination.size()-1);
            prev_ele = a[i];
        }
    }

	public List<List<Integer>> CombinationSum2(int a[], int n, int k){
		// Code Here.
		Arrays.sort(a);
		List<List<Integer>> ans = new ArrayList<List<Integer>>();
		List<Integer> combination = new ArrayList<Integer>();
        int index = 0;
        solve(a,index,combination,ans,k);
        return ans;
	}
}

