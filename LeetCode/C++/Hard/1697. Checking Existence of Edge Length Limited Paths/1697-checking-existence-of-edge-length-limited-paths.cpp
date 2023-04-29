class Solution {
public:
    vector<int>parent,size;
    void make(int var)
    {
        parent[var]=var;
        size[var]=1;
        return;
    }
    int findparent(int var)
    {
        if(parent[var]==var)
        {
            return var;
        }
        parent[var]=findparent(parent[var]);
        return parent[var];
    }
    void Union(int var1,int var2)
    {
        var1=findparent(var1);
        var2=findparent(var2);
        if(var1==var2)
        {
            return;
        }
        if(size[var1]>size[var2])
        {
            parent[var2]=var1;
            size[var1]+=size[var2];
        }
        else
        {
            parent[var1]=var2;
            size[var2]+=size[var1];
        }
        return;
    }
    static bool comparator(vector<int>&a,vector<int>&b)
    {
        return (a[2]<=b[2]);
    }
    vector<bool> distanceLimitedPathsExist(int n,vector<vector<int>>&edgeList,vector<vector<int>>&queries) 
    {
        parent.assign(n,0);
        size.assign(n,0);
        int i=0,j=0;
        for(i=0;i<n;i++)
        {
            make(i);
        }
        for(i=0;i<queries.size();i++)
        {
            queries[i].push_back(i);
        }
        vector<bool>ans(queries.size(),false);
        sort(edgeList.begin(),edgeList.end(),comparator);
        sort(queries.begin(),queries.end(),comparator);
        for(int i=0;i<queries.size();i++)
        {
            while(j<edgeList.size() && edgeList[j][2]<queries[i][2])
            {
                Union(edgeList[j][0],edgeList[j][1]);
                j++;
            }
            parent[queries[i][0]]=findparent(queries[i][0]);
            parent[queries[i][1]]=findparent(queries[i][1]);
            ans[queries[i][3]]=(parent[queries[i][0]]==parent[queries[i][1]]);
        }
        return ans;
    }
};