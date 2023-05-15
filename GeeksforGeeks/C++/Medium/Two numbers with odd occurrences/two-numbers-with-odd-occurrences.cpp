//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution{
    public:
    vector<long long int> twoOddNum(long long int Arr[], long long int N)  
    {
        // code here
        vector<long long int> ans;
        int res = 0;

        for (int i=0; i<N; i++) {
            res ^= Arr[i];
        }

        int mask = (res & (-res));
        int num1 = 0, num2 = 0;

        for (int j=0; j<N; j++) {
            if (Arr[j]&mask) {
                num1 ^= Arr[j];
            } else {
                num2 ^= Arr[j];
            }
        }

        if (num1>=num2) {
            ans.push_back(num1);
            ans.push_back(num2);
        } else {
            ans.push_back(num2);
            ans.push_back(num1);
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
        long long int N;
        cin>>N;
        long long int Arr[N];
        for(long int i = 0;i < N;i++)
        cin>>Arr[i];
        Solution ob;
        vector<long long int>ans=ob.twoOddNum(Arr,N);
        for(long long int i=0;i<ans.size();i++)cout<<ans[i]<<" ";
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends