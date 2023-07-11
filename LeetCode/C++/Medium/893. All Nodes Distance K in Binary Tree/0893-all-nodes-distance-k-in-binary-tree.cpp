/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode *root, map<int, vector<int>>&mp){
        if(!root)
            return;
        if(root -> left){
            mp[root -> val].push_back(root -> left -> val);
            mp[root -> left -> val].push_back(root -> val);
        }
        if(root -> right){
            mp[root -> val].push_back(root -> right -> val);
            mp[root -> right -> val].push_back(root -> val);
        }
        dfs(root -> left, mp);
        dfs(root -> right, mp);
    }
    void traverse(int node, map<int, vector<int>>&mp, int distance, int k, vector<int>&ans, unordered_map<int, bool>&vis){
        distance++;
        if(distance > k)
            return;
        vis[node] = true;
        for(int child: mp[node]){
            if(!vis[child]){
                vis[child] = true;
                if(distance == k){
                    ans.push_back(child);
                    continue;
                }
                traverse(child, mp, distance, k, ans, vis);
            }
        }
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        map<int, vector<int>>mp;
        dfs(root, mp);
        vector<int>ans;
        if(k == 0)
            return {target -> val};
        unordered_map<int, bool>vis;
        traverse(target -> val, mp,  0, k, ans, vis);
        return ans;
    }
};