//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int save_gotham(int arr[], int n);



int main() {
    
    int t;
    cin>> t;
    while(t--)
    {
        int n;cin>>n;
        int arr[n];
        
        for(int i=0;i<n;i++)
            cin>>arr[i];
        
        cout << save_gotham(arr, n) << endl;
    }
    
	return 0;
}
// } Driver Code Ends


int save_gotham(int arr[], int n)
{
    // Complete the function
    stack<int> s;
    vector<int> nxt(n,0);
    for(int i=n-1;i>=0;i--){
        while(!s.empty() && s.top()<=arr[i]){
            s.pop();
        }
        if(!s.empty()){
            nxt[i]=s.top();
        }
        s.push(arr[i]);
    }
    long long res=0;
    for(auto c: nxt){
        res+=c;
        res%=1000000007;
    }
    return res;
}