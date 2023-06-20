//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class segment_tree{
  
  public:
  vector<int> seg;
  segment_tree(int n){
      seg.resize(4*n);
  }
  void build(int ind,int l,int r,int a[],int lv){
      if(l==r){
          seg[ind] = a[l];
          return;
      }
      int mid = (l+r)>>1;
      build(2*ind+1,l,mid,a,lv-1);
      build(2*ind+2,mid+1,r,a,lv-1);
      if(lv&1){
          seg[ind] = seg[2*ind+1] | seg[2*ind+2];
      }
      else{
          seg[ind] = seg[2*ind+1] ^ seg[2*ind+2];
      }
  }
  void update(int ind,int l,int r,int lv,int key,int val){
      if(l==r){
          seg[ind] = val;
          return;
      }
      int mid = (l+r)>>1;
      if(key <= mid){
          update(2*ind+1,l,mid,lv-1,key,val);
      }
      else{
          update(2*ind+2,mid+1,r,lv-1,key,val);
      }
      if(lv&1){
          seg[ind] = seg[2*ind+1] | seg[2*ind+2];
      }
      else{
          seg[ind] =  seg[2*ind+1] ^ seg[2*ind+2];
      }
  }
  
};

class Solution{
public:
    vector<int> left(int n, int a[], int q, vector<pair<int, int>> queries)
    {
        // code here
        vector<int> ans;
        segment_tree s1(n);
        int lv = log2(n);
        s1.build(0,0,n-1,a,lv);
        for(int i = 0;i<q;i++){
            if(queries[i].first >= n or queries[i].first < 0) ans.push_back(-1);
            else{
                s1.update(0,0,n-1,lv,queries[i].first,queries[i].second);
                ans.push_back(s1.seg[0]);
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N, q;
        cin>>N;
        int A[N];
        for(int i = 0;i < N;i++)
            cin>>A[i];
        cin>>q;
        vector<pair<int,int>> query(q);
        int x, y;
        for(int i = 0;i < q;i++){
            cin>>x>>y;
            query[i] = {x, y};
        }
        
        Solution ob;
        vector<int> ans = ob.left(N, A, q, query);
        for(int u: ans)
            cout<<u<<"\n";
    }
    return 0;
}
// } Driver Code Ends