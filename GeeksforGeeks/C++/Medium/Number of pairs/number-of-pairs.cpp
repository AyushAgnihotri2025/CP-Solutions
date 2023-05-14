//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
 

class Solution{
    public:
    
    // X[], Y[]: input array
    // M, N: size of arrays X[] and Y[] respectively
    //Function to count number of pairs such that x^y is greater than y^x.
    long long countPairs(int X[], int Y[], int M, int N)
    {
       //Your code here
       sort(Y,Y+N);
       int count1 = 0 , count2 = 0, count3 = 0, count4 = 0;
       for(int i=0;i<N;i++){
           if(Y[i] == 1)       count1++;
           else if(Y[i] == 2 ) count2++;
           else if(Y[i] == 3)  count3++;
           else if(Y[i] == 4)  count4++;
       }
       long long int count = 0;
       for(int i=0;i<M;i++){
           int val = X[i];
           if(val == 1) continue;
           else if(val == 2){
               int ind = upper_bound(Y,Y+N,val) - Y;
               count += (N - ind);
               count += count1;
               count -= count3;
               count -= count4;
           }
           else if(val == 3){
               count += (N - count3);
           }
           else {
               int ind = upper_bound(Y,Y+N,val) - Y;
               count += (N-ind);
               count += count1;
           }
       }
       return count;
    }
};


//{ Driver Code Starts.
int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int M,N;
		cin>>M>>N;
		int i,a[M],b[N];
		for(i=0;i<M;i++)
		{
			cin>>a[i];
		}
		for(i=0;i<N;i++)
		{
			cin>>b[i];
		}
		Solution ob;
		cout<<ob.countPairs(a, b, M, N)<<endl;
	}
}
// } Driver Code Ends