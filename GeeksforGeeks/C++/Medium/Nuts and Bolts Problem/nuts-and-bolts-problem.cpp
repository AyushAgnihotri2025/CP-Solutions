//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	

	void matchPairs(char nuts[], char bolts[], int n) {
	    // code here
	    sort(nuts,nuts+n);
	    sort(bolts,bolts+n);
	    int l = 0, r = 1;
	    while(r<n){
	        while(bolts[l]==bolts[r] && r<n){
	            r++;
	        }
	        bolts[l+1] = bolts[r];
	        l++;
	        r++;
	    }
	    r = 1;
	    while(r<n){
	        while(nuts[l]==nuts[r] && r<n){
	            r++;
	        }
	        nuts[l+1] = nuts[r];
	        l++;
	        r++;
	    }
	    return;
	}

};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        char nuts[n], bolts[n];
        for (int i = 0; i < n; i++) {
            cin >> nuts[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> bolts[i];
        }
        Solution ob;
        ob.matchPairs(nuts, bolts, n);
        for (int i = 0; i < n; i++) {
            cout << nuts[i] << " ";
        }
        cout << "\n";
        for (int i = 0; i < n; i++) {
            cout << bolts[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends