//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    vector<char> easyTask(int n,string s,int q,vector<vector<string>> &queries){
        // Code here
        vector<char> ans;
        for(const auto & query : queries){
            if(query[0] == "1"){
                int ind = stoi(query[1]);
                s[ind] = query[2][0];
            }
            else if(query[0] == "2"){
                int arr[26] = {0};
                int left = stoi(query[1]);
                int right = stoi(query[2]);
                int k = stoi(query[3]);
                for(int i=left; i<=right; i++){
                    arr[s[i]-'a'] += 1;
                }
                for(int i=25; i>=0; i--){
                    k -= arr[i];
                    if(k <= 0){
                        ans.push_back('a'+i);
                        break;
                    }
                }
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        int q;
        cin>>q;
        vector<vector<string>> queries(q);
        for(int i=0;i<q;i++){
            string x;
            cin>>x;
            if(x=="1"){
                string p,q;
                cin>>p>>q;
                queries[i]={"1",p,q};
            }
            else{
                string p,q,r;
                cin>>p>>q>>r;
                queries[i]={"2",p,q,r};
            }
        }
        Solution ob;
        vector<char> ans=ob.easyTask(n,s,q,queries);
        for(auto ch:ans){
            cout<<ch<<" ";
        }
        cout<<endl;
    }
}

// } Driver Code Ends