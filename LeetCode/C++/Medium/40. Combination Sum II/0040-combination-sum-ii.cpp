class Solution {
 	int target_;

 	void recursion(vector<int>& candidates, int index, int sum, vector<int>& cur, vector<vector<int>>& res_){
 		if(target_ == sum) res_.push_back(cur);
 		else if(sum < target_){
 			int size = candidates.size();
 			for(int i = index; i < size; ++i){
 				while(i > index && i < size && candidates[i] == candidates[i - 1]) ++i;
 				if(i >= size) break;
 				cur.emplace_back(candidates[i]);
 				recursion(candidates, i + 1, sum + candidates[i], cur, res_);
 				cur.pop_back();
 			}
 		}
 	}

public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
 		if(candidates.empty()) return {};
 		sort(candidates.begin(), candidates.end());
 		vector<vector<int>> res_;   
 		vector<int> cur;
 		target_ = target;
 		recursion(candidates, 0, 0, cur, res_);
 		return res_;
 	}
};