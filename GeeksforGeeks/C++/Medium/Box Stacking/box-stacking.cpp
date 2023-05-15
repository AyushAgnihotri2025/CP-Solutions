//{ Driver Code Starts
#include<bits/stdc++.h>

using namespace std;

// } Driver Code Ends

class Solution {
    public:
        /*The function takes an array of heights, width and 
        length as its 3 arguments where each index i value 
        determines the height, width, length of the ith box. 
        Here n is the total no of boxes.*/
        int maxHeight(int height[], int width[], int length[], int n) {
            //Your code here
            vector<vector<int>> boxes;
            for (int i = 0; i < n; i++) {
                boxes.push_back({
                    length[i],
                    width[i],
                    height[i]
                });
                boxes.push_back({
                    length[i],
                    height[i],
                    width[i]
                });
                boxes.push_back({
                    width[i],
                    length[i],
                    height[i]
                });
                boxes.push_back({
                    width[i],
                    height[i],
                    length[i]
                });
                boxes.push_back({
                    height[i],
                    length[i],
                    width[i]
                });
                boxes.push_back({
                    height[i],
                    width[i],
                    length[i]
                });
            }

            sort(boxes.begin(), boxes.end(), [](vector<int> a, vector<int> b) {
                return (a[0] * a[1]) > (b[0] * b[1]);
            });

            int dp[boxes.size()];
            for (int i = 0; i < boxes.size(); i++) {
                dp[i] = boxes[i][2];
                for (int j = 0; j < i; j++) {
                    if (boxes[j][0] > boxes[i][0] && boxes[j][1] > boxes[i][1]) {
                        dp[i] = max(dp[i], dp[j] + boxes[i][2]);
                    }
                }
            }
            int ans = 0;
            for (int i = 0; i < boxes.size(); i++) {
                ans = max(ans, dp[i]);
            }
            return ans;
        }
};

//{ Driver Code Starts.

int main() {
	int t;
	cin>>t;
	while(t--)
	{
        int n;
        cin>>n;
        
    
        int A[105],B[105],C[105];
        for(int i = 0; i < n; i++)cin >> A[i];
        for(int j = 0; j < n; j++)cin >> B[j];
        for(int k = 0; k < n; k++)cin >> C[k];
        Solution ob;
        cout<<ob.maxHeight(A,B,C,n)<<endl;
    }
	
	return 0;
}
	
// } Driver Code Ends