//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class Node
{
    int data;
    Node next;
    public Node(int data)
    {
        this.data=data;
    }
}
class GFG{
    public static void main(String args[]) throws IOException { 
        BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int t = Integer.parseInt(in.readLine());

        while (t-- > 0) {
            int n=Integer.parseInt(in.readLine().trim());
            String s[]=in.readLine().trim().split(" ");
            Node head=new Node(Integer.parseInt(s[0]));
            Node copy=head;
            for(int i=1;i<n;i++){
                Node temp=new Node(Integer.parseInt(s[i]));
                copy.next=temp;
                copy=copy.next;
            }
            Solution ob=new Solution();
            Node ans=ob.modifyTheList(head);
            while(ans!=null){
                out.print(ans.data+" ");
                ans=ans.next;
            }out.println();
        }
        out.close();
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution
{
    public static Node modifyTheList(Node head)
    {
        if(head==null || head.next==null) return head;
        ArrayList<Integer> arr=new ArrayList<>();
        Node temp=head;
        while(temp!=null){
            arr.add(temp.data);
            temp=temp.next;
        }
        int j=arr.size()-1;
        temp=head;
        Node dummy=new Node(-1);
        Node curr=dummy;
        int size=(arr.size()/2)-1;
        for(int i=0;i<=size;i++){
            int subtract=arr.get(j)-arr.get(i);
            Node t=new Node(subtract);
            curr.next=t;
            curr=curr.next;
            j--;
        }
        if(arr.size()%2!=0) size+=1;
        for(int i=size;i>=0;i--){
            Node t=new Node(arr.get(i));
            curr.next=t;
            curr=curr.next;
        }
        return dummy.next;
    }
}