//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class GFG{
	public static void main(String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int test = Integer.parseInt(br.readLine());
		while(test-- > 0) {
			int n = Integer.parseInt(br.readLine());
			int [] arr = new int[n];
			String [] str = br.readLine().trim().split(" ");
			for(int i = 0; i < n; i++)
				arr[i] = Integer.parseInt(str[i]);
			Solution ob = new Solution();
			int [] ans = ob.nearestSmallestTower(arr);
			for(int i = 0; i < n; i++)
				System.out.print(ans[i]+" ");
			System.out.println();
		}
		
	}
}
// } Driver Code Ends


//User function Template for Java


class Solution{
	int [] nearestSmallestTower(int [] arr){
		//Write your code here
		int[] sol1 = nextSmlLeft(arr);
		int[] sol2 = nextSmlRight(arr);
		
		int[] sol = new int[arr.length];
		
		for(int i=0; i<arr.length; i++){
		    //They both don't have smallest element neither in left nor in right
		    if(sol1[i] == sol2[i]){
		        sol[i] = sol1[i];
		    }else if(sol1[i] == -1 || sol2[i] == -1){ //Smallest element is either in left or in right
		        sol[i] = sol1[i] > sol2[i] ? sol1[i] : sol2[i];
		    }else if(i - sol1[i] > sol2[i] - i){
		        sol[i] = sol2[i];
		    }else if(i - sol1[i] < sol2[i] -i){
		        sol[i] = sol1[i];
		    }else{
		       sol[i] = arr[sol1[i]] > arr[sol2[i]] ? sol2[i] : sol1[i];
		    }
		}
		return sol;
	}
	
	int[] nextSmlLeft(int[] arr){
	    int[] sol = new int[arr.length];
	    Stack<Integer> st = new Stack<>();
	    
	    sol[0] = -1;
	    st.push(0);
	    
	    for(int i=1; i<arr.length; i++){
	        while(st.size() > 0 && arr[i] <= arr[st.peek()]){
	            st.pop();
	        }
	        if(st.size() == 0){
	            sol[i] = -1;
	        }else{
	            sol[i] = st.peek();
	        }
	        st.push(i);
	    }
	    return sol;
	}
	
	int[] nextSmlRight(int[] arr){
	    int[] sol = new int[arr.length];
	    Stack<Integer> st = new Stack<>();
	    
	    sol[arr.length - 1] = -1;
	    st.push(arr.length - 1);
	    
	    for(int i=arr.length - 2; i>=0; i--){
	        while(st.size() > 0 && arr[i] <= arr[st.peek()]){
	            st.pop();
	        }
	        if(st.size() == 0){
	            sol[i] = -1;
	        }else{
	            sol[i] = st.peek();
	        }
	        st.push(i);
	    }
	    return sol;
	}
}