//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
        vector <int> search(string pat, string txt)
        {
            //code here.
            vector<int>ans;
            for(int i=0;i<=txt.length()-pat.length();i++)
            {
                if(pat==txt.substr(i,pat.length()))
                ans.push_back(i+1);
            }
            if(ans.size()!=0) return ans;
            else {
                ans.push_back(-1);
                return ans;
            }
        }
     
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S, pat;
        cin >> S >> pat;
        Solution ob;
        vector <int> res = ob.search(pat, S);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}

// Contributed By: Pranay Bansal

// } Driver Code Ends