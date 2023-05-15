//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++



class Solution{   
public:
    int maxSubarrayXOR(int N, int arr[]){    
        //code here
        int ans = 1 , max_sum = INT_MIN;
        for(int i=0; i < N; ++i){
            if(N==1) 
                return arr[0];
            if(arr[i] == arr[i+1]) 
            max_sum=arr[i];
            ans = max(arr[i] , arr[i] ^ ans);
            max_sum = max(max_sum , ans);
        }
        return max_sum;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N, X;
        cin >> N;
        int arr[N];
        for(int i = 0; i < N; i++){
            cin >> arr[i];
        }

        Solution ob;
        cout << ob.maxSubarrayXOR(N, arr) << endl;
    }
    return 0; 
} 

// } Driver Code Ends