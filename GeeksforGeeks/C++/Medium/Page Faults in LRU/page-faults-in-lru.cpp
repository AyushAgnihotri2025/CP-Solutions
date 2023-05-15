//{ Driver Code Starts
// Initial Template for C++



#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int pageFaults(int N, int C, int a[]){
        // code here
        vector<pair<int ,int>> page_array;
       int fault=0;
       int flag=0;
       for(int i=0;i<N;++i){
           flag=0;
           int max_index=INT_MIN;
           int replace=-1;
           for(int j=0;j<page_array.size();++j){
               if(page_array[j].first==a[i] && flag==0){
                   page_array[j].second=1;
                   flag=1;
                   continue;
               }
               page_array[j].second++;
               if(max_index<page_array[j].second){
                   max_index=page_array[j].second;
                   replace=j;
               }
           }
           if(!flag){
               fault++;
               if(page_array.size()<C){
                   page_array.push_back(make_pair(a[i],1));
               }
               else{
                   page_array[replace].first=a[i];
                   page_array[replace].second=1;
               }
           }
       }
       return fault;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N, C;
        cin>>N;
        int pages[N];
        for(int i = 0;i < N;i++)
            cin>>pages[i];
        cin>>C;
        
        Solution ob;
        cout<<ob.pageFaults(N, C, pages)<<"\n";
    }
    return 0;
}
// } Driver Code Ends