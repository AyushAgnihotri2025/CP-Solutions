//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

int countRev (string s);
int main()
{
    int t; cin >> t;
    while (t--)
    {
        string s; cin >> s;
        cout << countRev (s) << '\n';
    }
}

// Contributed By: Pranay Bansal
// } Driver Code Ends


int countRev (string s)
{
    // your code here
    int count=0,ans=0;
    stack<int> st;
    for(auto it:s){
        if(it=='{')
            st.push(it);
        else if( it=='}' && !st.empty()){
            st.pop();
        }
        else{
            count++;
        }
    }
    ans+=(count/2)+(st.size()/2);
    if(count%2!=st.size()%2) return -1;
    return ans+(count%2)+(st.size()%2);
}