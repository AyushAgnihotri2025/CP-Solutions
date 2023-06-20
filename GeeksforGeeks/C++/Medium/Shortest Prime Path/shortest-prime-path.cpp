//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution{ 
    public:
        vector<bool>isprime;
        void seive(vector<int>&v){
            int N=10005;
            isprime.resize(N+1,true);
            isprime[0]=isprime[1]=false;
            for(int i=2;i<=N;i++){
                if(isprime[i]==true){
                    for(int j=i*i;j<=N;j+=i){
                        isprime[j]=false;
                    }
                }
            }
            for(int i=1000;i<10000;i++){
                if(isprime[i])v.push_back(i);
            }
        }
        int solve(int Num1,int Num2)
        {   
            //code here
            vector<int>v;
            seive(v);
            int n=v.size();
            vector<int>vis(10000,0);
            queue<pair<int,int>>q;
            q.push({0,Num1});
            vis[Num1]=1;
            while(!q.empty()){
             auto it=q.front();
             q.pop();
             int lvl=it.first;
             int node=it.second;
             string s=to_string(node);
             if(node==Num2)return lvl;
             for(int i=0;i<4;i++){
                 char original=s[i];
                 for(char ch='0';ch<='9';ch++){
                     if(i==0&&ch=='0')continue;
                     s[i]=ch;
                     int number=stoi(s);
                     if(number==Num2)return lvl+1;
                     if(isprime[number]&&vis[number]==0)q.push({lvl+1,number});
                     vis[number]=1;
                }
                s[i]=original;
            }
        }
        return -1;
    }
};


//{ Driver Code Starts.
signed main()
{
  int t;
  cin>>t;
  while(t--)
  {
      int Num1,Num2;
      cin>>Num1>>Num2;
      Solution obj;
      int answer=obj.solve(Num1,Num2);
      cout<<answer<<endl;
  }
}
// } Driver Code Ends