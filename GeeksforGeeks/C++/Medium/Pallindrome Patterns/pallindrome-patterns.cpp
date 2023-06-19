//{ Driver Code Starts



#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution
{
	public:
		vector<string> all_plaindromes(string s)
		{
		    // Code here
		    string alp="abcdefghijklmnopqrstuvwxyz";
		    vector<int> ch(26,0);
		    string res="";
		    vector<string> ans;
		    for(int i=0;i<s.length();i++){
		        int t=s[i]-'a';
		        ch[t]++;
		    }
		    string pos="";
		    for(int i=0;i<26;i++){
		        int temp=ch[i];
		        if(temp%2==1) pos+=alp[i];
		        while(temp>1){
		            res+=alp[i];
		            temp-=2;
		        }
		    }
		    if(pos.size()>1) return {};
		    string restemp=res;
		    do{
		        string res2=restemp;
		        reverse(res2.begin(), res2.end());
		        ans.push_back(restemp+pos+res2);
		        next_permutation(restemp.begin(),restemp.end());
		    }while(restemp!=res);
		    return ans;
		}
};



//{ Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	string s;
    	cin >> s;
        Solution ob;
    	vector<string> ans  = ob.all_plaindromes(s);
    	cout<<"{ ";
    	for(auto i: ans)
    		cout << i << " ";
    	cout<<"}";
    	cout<<"\n";
    }
	return 0;
}


// } Driver Code Ends