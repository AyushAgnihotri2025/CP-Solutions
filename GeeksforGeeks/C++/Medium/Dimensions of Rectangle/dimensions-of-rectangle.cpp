//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int rectangleCount(int A){
        // code here
        int i=1;
        int j=A;
        int count=0;
       while(i<=j)
       {   
           if(i*j==A)
           {  
               if(i%2==0 && j%2==0){
                   if(i==j)
                   count++;
               }
               else if(i%2 !=0 || j%2!=0)
               count++;
               i++;
               j--;
           }
           else if(i*j>A)
           j--;
           else
           i++;
       }
        return count;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int A;
        cin>>A;
        
        Solution ob;
        cout<<ob.rectangleCount(A)<<"\n";
    }
    return 0;
}
// } Driver Code Ends