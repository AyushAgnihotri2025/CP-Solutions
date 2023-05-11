//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution 
{
    public:
    //Function to find out minimum steps Knight needs to reach target position.
	int minStepToReachTarget(vector<int>&KnightPos,vector<int>&TargetPos,int N)
	{
	    // Code here
	    using p=pair<int,int>;
        vector<vector<int>>vis(N,vector<int>(N,0));
        queue<p>q;
        q.push({KnightPos[0]-1,KnightPos[1]-1});
        vis[KnightPos[0]-1][KnightPos[1]-1]=1;
        int step=0;
        int cx[8]={2,2,-2,-2,1,1,-1,-1};
        int cy[8]={1,-1,1,-1,2,-2,2,-2};
        while(!q.empty())
        {
          int n=q.size();
          while(n--)
          {
              int x=q.front().first;
              int y=q.front().second;
              q.pop();
              if(x==TargetPos[0]-1 && y==TargetPos[1]-1) return step;
              
              for(int i=0;i<8;i++)
              {
                  int X=x+cx[i];
                  int Y=y+cy[i];
                  if(X<0 || Y<0 || X>=N || Y>=N || vis[X][Y]==1) continue;
                  vis[X][Y]=1;
                  q.push({X,Y});
              }
          }
          step++;
          
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