//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++

class Solution
{
    public:
    //Function to find most frequent word in an array of strings.
    string mostFrequentWord(string arr[], int n) 
    {
        // code here
        unordered_map<string,int>count,mp;
        for(int i=0;i<n;i++){
            count[arr[i]]++;
            if(mp.find(arr[i])==mp.end())
                mp[arr[i]]=i;
        }
        int res=0;
        string ans;
        int ans_ind=0;
        for(auto x:count){
            string a=x.first;
            int b=x.second;
            if(res<b){
                res=b;
                ans=a;
                ans_ind=mp[a];
            }
            else if(res==b){
                if(mp[a]>ans_ind){
                    ans=a;
                    ans_ind=mp[a];
                }
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        string arr[n];
        for (int i = 0; i < n; i++) cin >> arr[i];
        Solution obj;
        cout << obj.mostFrequentWord(arr, n) << endl;
    }
    return 0;
}

// } Driver Code Ends