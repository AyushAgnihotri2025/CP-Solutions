//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	int isRepeat(string s)
	{
	    // Your code goes here
        string ans="";
        int n=s.length();
        for(int i=0;i<n/2;i++){
            ans+=s[i];
            int k=0;
            bool f=true;
            for(int j=i+1;j<n && f;j++){
                if(ans[k]!=s[j])
                    f=false;
                k=(k+1)%(ans.length());
            }
            
            if(f && k==0){
            return 1;
            }
        }
        return 0;
	}
};

//{ Driver Code Starts.

int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string str;
   		cin >> str;
        Solution ob;
   		cout << ob.isRepeat(str) << "\n";
   	}

    return 0;
}
// } Driver Code Ends