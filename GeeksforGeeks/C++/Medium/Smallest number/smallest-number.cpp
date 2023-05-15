//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends

class Solution{   
public:
    string smallestNumber(int s, int d){
        // code here 
        string ans(d, '0');

        if (d * 9 < s) return "-1";

        int i = d - 1;
        ans[0] = '1';
        s -= 1;
        while (i >= 0 && s > 0) {
            if (s > 9) {
                ans[i] = '9';
                s -= 9;
                i--;
            } else {
                if (i == 0) {
                    s++;
                }
                string str = to_string(s);
                ans[i--] = str[0];
                s -= s;
            }
        }
        return ans;
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int S,D;
        cin >> S >> D;
        Solution ob;
        cout << ob.smallestNumber(S,D) << endl;
    }
    return 0; 
} 
// } Driver Code Ends