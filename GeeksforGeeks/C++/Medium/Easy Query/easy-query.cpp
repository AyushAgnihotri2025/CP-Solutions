//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class ST{
    vector<int> *tree;
    public:
    ST(int n){
        tree=new vector<int>[4*n+1];
    }
    void merge(int lc,int rc,int curr){
        int n=tree[lc].size(), m=tree[rc].size(),i=0,j=0;
        for(i,j;i<n && j<m;){
            if(tree[lc][i]<tree[rc][j])
                tree[curr].push_back(tree[lc][i++]);
            else
                tree[curr].push_back(tree[rc][j++]);
        }
        while(i<n)
            tree[curr].push_back(tree[lc][i++]);
        while(j<m)
            tree[curr].push_back(tree[rc][j++]);
    }
    void build(int node,int start,int end,vector<pair<int,int>> &a){
        if(start==end){
            tree[node].push_back(a[start-1].second);
            return;
        }
        int mid = (start+end)>>1, lc=node<<1, rc= lc|1;
        build(lc,start,mid,a);
        build(rc,mid+1,end,a);
        merge(lc,rc,node);
    }
    int query(int node,int start,int end,int l,int r,int k){
        if(start==end)
            return tree[node][0];
        int mid=(start+end)>>1, lc=(node<<1), rc=lc|1;
        int lLoc = lower_bound(tree[lc].begin(),tree[lc].end(),l)-tree[lc].begin();
        int rLoc = upper_bound(tree[lc].begin(),tree[lc].end(),r)-tree[lc].begin();
        
        int range = rLoc-lLoc;
        if(range>=k)
            return query(lc,start,mid,l,r,k);
        else
            return query(rc,mid+1,end,l,r,k-range);
    }
};
class Solution {
public:
	vector<int>FindQuery(vector<int>b, vector<vector<int>>Q){
	    // Code here
	    int n=b.size();
	    vector<pair<int,int>> a;
	    for(int i=0;i<n;i++)
	        a.push_back({b[i],i+1});
	    sort(a.begin(),a.end());
	    ST st(n);
	    st.build(1,1,n,a);
	    vector<int> ans;
	    for(int i=0;i<Q.size();i++){
	        int l=Q[i][0], r=Q[i][1], k=Q[i][2];
	        ans.push_back(b[st.query(1,1,n,l,r,k)-1]);
	    }
	    return ans;
	}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, q;
		cin >> n >> q;
		vector<int>nums(n);
		for(int i = 0; i < n; i++)
			cin >> nums[i];
		vector<vector<int>>Query;
		for(int i = 0; i < q; i++){
			int l, r, k;
			cin >> l >> r >> k;
			Query.push_back({l, r, k});
		}
		Solution obj;
		vector<int>ans = obj.FindQuery(nums, Query);
		for(auto i: ans)
			cout << i << "\n";
	}
	return 0;
}
// } Driver Code Ends