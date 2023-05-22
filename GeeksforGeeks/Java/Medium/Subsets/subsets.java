//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCases = sc.nextInt();
		for(int t=0;t<testCases;t++){
		    int n = sc.nextInt();
		    int arr[] = new int[n];
		    ArrayList<Integer> A = new ArrayList<Integer>();
		    for(int i=0;i<n;i++){
		        arr[i] = sc.nextInt();
		        A.add(arr[i]);
		        
		    }
		   
		   
		    
		    ArrayList <ArrayList<Integer>> res = new Solution().subsets(A);
		    for (int i = 0; i < res.size (); i++)
		    {
		        for (int j = 0; j < res.get(i).size (); j++)
		        {
		          System.out.print(res.get(i).get(j)+" ");
		        }
		        System.out.println();
		      
		    }
		    //System.out.println();
		}
	}
}
// } Driver Code Ends


//User function Template for Java
class comp implements Comparator<ArrayList<Integer>>{
    public int compare(ArrayList<Integer> a,ArrayList<Integer> b){
        int n=Math.min(a.size(),b.size());
        for(int i=0;i<n;i++){
            if(a.get(i)!=b.get(i)){
                return a.get(i)-b.get(i);
            }
        }
        return a.size()-b.size();
    }
}

class Solution
{
    public static ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> A)
    {
        //code here
        ArrayList<ArrayList<Integer>> res=new ArrayList<>();
        for(int i=0;i<(1<<A.size());i++){
            ArrayList<Integer> ds=new ArrayList<>();
            for(int bits=0;bits<A.size();bits++){
                if((i&(1<<bits))!=0){
                    ds.add(A.get(bits));
                }
            }
            res.add(new ArrayList<>(ds));
        }
        Collections.sort(res,new comp());
        return res;
    }
}