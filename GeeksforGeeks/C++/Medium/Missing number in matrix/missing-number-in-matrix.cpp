//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
public:
    long long int MissingNo(vector<vector<int> >& matrix) {
        // Code here
        int a = -1, b = -1;
        int n = matrix.size();
        long row[n], col[n], d1 = 0, d2 = 0;
        for (int i = 0; i < n; i++)
            row[i] = col[i] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                row[i] += matrix[i][j];
                col[j] += matrix[i][j];
                if (matrix[i][j] == 0) {
                    a = i;
                    b = j;
                }
                if (i == j)
                    d1 += matrix[i][j];
                if (i == n - j - 1)
                    d2 += matrix[i][j];
            }
        }
        if (a == -1 || row[a] != col[b])
            return -1;
        if (a != b && a != n - b - 1 && d1 != d2)
            return -1;
        long r = row[0];
        if (a == 0)
            r = row[n - 1];
        long res = r - row[a];
        if (r < row[a] || r < col[b] || res == 0)
            return -1;
        for (int i = 0; i < n; i++) {
            if (a != i && row[i] != r)
                return -1;
            if (b != i && col[i] != r)
                return -1;
        }
        if (a == b && a == n - b - 1 && d1 != d2)
            return -1;
        if (a == b && a != n - b - 1 && res + d1 != d2)
            return -1;
        if (a != b && a == n - b - 1 && res + d2 != d1)
            return -1;
        return res;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>> matrix(n, vector<int>(n,0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> matrix[i][j];
			}
		}
		Solution ob;
		long long int ans = ob.MissingNo(matrix);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends