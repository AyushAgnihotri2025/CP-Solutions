//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution{
public:	
		
	int isDivisible(string s){
	    //complete the function here
        int state = 0;
        int transitions[2][3] = {
            {0, 2, 1}, 
            {1, 0, 2}
        };

        for (char c : s)
            state = transitions[c - '0'][state];
        
        return state == 0;
	}
};

//{ Driver Code Starts.
int main(){
    
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        Solution ob;
        cout << ob.isDivisible(s) << endl;
    }
return 0;
}


// } Driver Code Ends