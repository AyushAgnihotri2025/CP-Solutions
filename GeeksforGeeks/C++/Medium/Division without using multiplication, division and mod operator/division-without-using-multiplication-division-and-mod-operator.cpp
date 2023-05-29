//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    long long divide(long long dividend, long long divisor) 
    {
        //code here
       int a =dividend,b=divisor;
       dividend= abs(dividend);
       divisor= abs(divisor);
       long long quotient=0;
       for(int i=32;i>=0;i--)
       {
             if((divisor<<i)<=dividend)
             {
                 dividend -= (divisor<<i);
                 quotient |= 1<<i;
             }
       }
       if(((a<0)&&(b<0))||((a>0)&&(b>0)))
       return quotient;
       else
       return -quotient;
    }
};

//{ Driver Code Starts.
int main() {
	int t;
	cin >> t;

	while (t--)
	{

		long long a, b;
		cin >> a >> b;
		
		Solution ob;
		cout << ob.divide(a, b) << "\n";
	}

	return 0;
}

// } Driver Code Ends