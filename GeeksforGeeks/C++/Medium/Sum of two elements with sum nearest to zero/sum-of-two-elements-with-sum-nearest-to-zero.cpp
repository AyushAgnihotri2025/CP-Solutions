//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
        int closestToZero(int arr[], int n)
        {
            // your code here 
            sort(arr, arr+n);
            int i=0, j=n-1, max_ans=INT_MAX;
            while(i<j){
                if(abs(max_ans)>abs(arr[i]+arr[j])){
                    max_ans=arr[i]+arr[j];
                }
                else if(abs(max_ans)==abs(arr[i]+arr[j])){
                    max_ans=max(max_ans, arr[i]+arr[j]);
                }
                
                if(arr[i]+arr[j]>0) j--;
                else i++;
            }
            
            return max_ans;
        }
};

//{ Driver Code Starts.
int main ()
{
    int t; 
    cin >> t;
    while (t--)
    {
        int n; 
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        Solution ob;
        cout << ob.closestToZero(arr, n) << endl;
    }
}
// } Driver Code Ends