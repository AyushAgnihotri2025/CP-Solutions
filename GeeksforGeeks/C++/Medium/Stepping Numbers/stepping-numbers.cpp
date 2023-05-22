//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
public:

    int steppingNumbers(int n, int m)
    {
        // Code Here
        queue<int>q;
        for(int i=0;i<=9;i++) q.push(i);
        int cnt = 0;
        while(!q.empty()){
            int num = q.front();
            q.pop();
            if(num>=n && num<=m){
                cnt++;
            }
            int b = num*10+1;
            int ld = num%10;
            if(num==0) continue;
            int val1 = num*10+(num%10)-1;
            int val2 = num*10+(num%10)+1;
            if(ld==0){
                if(val2<=m && val2>9) q.push(val2);
            }
            else if(ld==9){
                if(val1<=m && val1>9) q.push(val1);
            }
            else{
                if(val1<=m && val1>9) q.push(val1);
                if(val2<=m && val2>9) q.push(val2);
            }
        }
        return cnt;
    }
};


//{ Driver Code Starts.

int main()
{
    
    int t;
    cin>>t;
    while(t--)
    {
        Solution obj;
        int n, m;
        cin>>n>>m;
        cout << obj.steppingNumbers(n,m) << endl;
    }
	return 0;
}


// } Driver Code Ends