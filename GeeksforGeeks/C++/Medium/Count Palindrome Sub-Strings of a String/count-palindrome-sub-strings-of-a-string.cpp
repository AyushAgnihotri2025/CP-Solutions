//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

int CountPS(char S[], int N);

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        char S[N+1];
        cin>>S;
        cout<<CountPS(S,N)<<endl;
    }
    return 0;
}


// } Driver Code Ends


int CountPS(char S[], int N)
{
    //code here
    string s;
    for(int i=0;i<N;i++){
        s.push_back(S[i]);
    }
    int ans = 0;
    int l = 0;
    int r = 0;
    int n = s.size();
    for(int i=0;i<n;i++){
        l = r = i;
        while ( l >= 0 and r < n and s[l] == s[r]){
            l != r ?ans++ : NULL;
            l--;
            r++;
        }
        l = i;
        r = i+1;
        while ( l >= 0 and r < n and s[l] == s[r]){
            ans++;
            l--;
            r++;
        }
        
    }
    return ans;
    
    
}