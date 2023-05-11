//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
public:
	int minStepToReachTarget(vector<int>&KnightPos, vector<int>&TargetPos, int N){
	    // Code here
	    queue<pair<int,pair<int,int>>>q;
        q.push({0,{KnightPos[0],KnightPos[1]}});
        int dx[]={-2,-1,1,2};
        int dy[]={-2,-1,1,2};
        vector<vector<int>>vis(1000,vector<int>(1000,0));
        vis[KnightPos[0]][KnightPos[1]]=1;
        int ans=0;
        while(!q.empty())
        {
         int i=q.front().second.first,j=q.front().second.second;
         int dist=q.front().first;
         
         q.pop();
         if(i==TargetPos[0] and j==TargetPos[1]) return dist;
         for(int p=0;p<4;p++){
             for(int r=0;r<4;r++){
                 if(abs(dx[p])==abs(dy[r])) continue;
                 int x=i+dx[p],y=j+dy[r];
                 if(x<=N and y<=N and x>0 and y>0 and !vis[x][y]){
                     vis[x][y]=1;
                     q.push({dist+1,{x,y}});
                     
                 }
             }
         }
         
        }
        return -1;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		vector<int>KnightPos(2);
		vector<int>TargetPos(2);
		int N;
		cin >> N;
		cin >> KnightPos[0] >> KnightPos[1];
		cin >> TargetPos[0] >> TargetPos[1];
		Solution obj;
		int ans = obj.minStepToReachTarget(KnightPos, TargetPos, N);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends