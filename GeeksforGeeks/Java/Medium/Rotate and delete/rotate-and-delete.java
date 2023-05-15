//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Main {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		
		while(t-->0){
		    int n = Integer.parseInt(br.readLine().trim());
		    ArrayList<Integer> arr = new ArrayList<Integer>(n);
		    String inputLine[] = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        arr.add(Integer.parseInt(inputLine[i]));
		    }
		    
		    Solution ob = new Solution();
		    
		    System.out.println(ob.rotateDelete(arr, n));
		    
		}
	}
}


// } Driver Code Ends



class Solution{
    
    // function to do operations of rotate and delete
    // arr: input array
    // n: size of Array
    public static int rotateDelete(ArrayList<Integer> arr, int n){
        // Your code here
        int indx = 0,sec_indx=0,last_indx = n-1;
        while(arr.size()!=1){
            int last_ele = arr.get(arr.size()-1);
            arr.add(0,last_ele);
            arr.remove(arr.size()-1);
            int delete_indx = last_indx-indx-sec_indx;
            if(delete_indx<0){
                delete_indx = 0;
            }
            arr.remove(delete_indx);
            indx++;
            sec_indx++;
        }
        return arr.get(0);
    }
}