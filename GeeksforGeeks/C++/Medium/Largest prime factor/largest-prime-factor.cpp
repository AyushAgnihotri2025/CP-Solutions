//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public: 
    long long int largestPrimeFactor(int N){
        // code here
        int n = 100000;
        bool sieve[100001];
        
        for(int i=0;i<n;++i){
            if(i==0 || i==1) sieve[i] = false;
            else sieve[i] = true;
        }
        
        for(int i=2;i*i<=n;++i){
            if(sieve[i] == true){
                for(int j=i*i;j<=n;j+=i){
                    sieve[j] = false;
                }
            }
        }
        
        vector<long long int> primes;
        for(int i=0;i<=n;++i){
            if(sieve[i] == true) primes.push_back(i);
        }
        
        for(int i=primes.size()-1;i>=0;--i){
            if(primes[i] == N) return N;
            else{
                if(N%primes[i] == 0){
                    return primes[i];
                }
            }
        }
        
        return -1;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.largestPrimeFactor(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends