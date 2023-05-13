//{ Driver Code Starts
//Initial Template for Java


import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
	public static void main(String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0)
        {
            String S = br.readLine().trim();
            int N = S.length();
            Solution ob = new Solution();
            String[] element = br.readLine().trim().split("\\s+");
		    int[] f = new int[N];
		    for(int i = 0; i < N; i++){
		        f[i] = Integer.parseInt(element[i]);
		    }
            ArrayList<String> res  = ob.huffmanCodes(S,f,N);
            for(int i = 0; i < res.size(); i++)
            {
                System.out.print(res.get(i)+" ");
            }
            System.out.println();
        }
	}
}
// } Driver Code Ends


//User function Template for Java

class Node{
   char ch;
   int freq;
   Node left;
   Node right;
   Node(char c, int f, Node l, Node r){
       ch = c;
       freq = f;
       left = l;
       right = r;
   }
}

class Solution {
    public ArrayList<String> huffmanCodes(String S, int f[], int N)
    {
        // Code here
        PriorityQueue<Node> p = new PriorityQueue<>((n1, n2)->{
            if(n1.freq==n2.freq)
                return 1;
            return  n1.freq-n2.freq;
            });
           
       
        for(int i=0; i<N; i++){
            p.add(new Node(S.charAt(i), f[i], null, null));
        }
       
        while(p.size()>1){
            Node l = p.poll();
            Node r = p.poll();
            p.add(new Node('$', l.freq+r.freq, l, r));
        }
       
        ArrayList<String> al = new ArrayList<>();
       
        printCodes(p.peek(),"", al);
       
        return al;
       
    }
   
    public static void printCodes(Node root,  String str, ArrayList<String> al){
        if(root==null)
            return;
          
        if(root.ch!='$'){
            al.add(str);
            return;
        }
       
        printCodes(root.left, str+"0", al);
        printCodes(root.right, str+"1", al);
   
    }
}