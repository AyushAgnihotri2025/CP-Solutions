//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> getPrimes(int N) {
        // code here
        int n = 1e6;
        bool sieve[n+1];
        
        for(int i=0;i<=n;++i){
            if(i==0 || i==1) sieve[i] = false;
            else sieve[i] = true;
        }
        for(int i=2;i*i<=n;++i){
            if(sieve[i]){
                for(int j=i*i;j<=n;j+=i){
                    sieve[j] = false;
                }
            }
        }
        vector<int> primes;
        for(int i=2;i<=n;++i){
            if(sieve[i]) primes.push_back(i);
        }
        vector<int> ans;
        int sz = primes.size();
        int s=0,e=sz-1;
        while(s < e){
            int sum = primes[s]+primes[e];
            if(sum == N){
                ans.push_back(primes[s]);
                ans.push_back(primes[e]);
                break;
            }else if(sum > N) e--;
            else s++;
        }
        if(!(ans.size())){
            ans.push_back(-1);
            ans.push_back(-1);
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;

        Solution ob;
        vector<int> ptr = ob.getPrimes(N);
        cout << ptr[0]<<" "<<ptr[1] << endl;
    }
    return 0;
}
// } Driver Code Ends