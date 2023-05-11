//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    int longestUniqueSubsttr(string S){
        //code
        int mp[26]={0};
        int i=0;
        int j=0;
        int ans=0;
        while(i<S.size()){
            if(mp[S[i]-'a']!=0){
                mp[S[j]-'a']--;
                j++;
            }
            else{
                mp[S[i]-'a']++;
                ans=max(ans,i-j+1);
                i++;
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
		string str;
		cin>>str;
		Solution ob;
		cout<<ob.longestUniqueSubsttr(str)<<endl;
	}
	return 0;
}
// } Driver Code Ends