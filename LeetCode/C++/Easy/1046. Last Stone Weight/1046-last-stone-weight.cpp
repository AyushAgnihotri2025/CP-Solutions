class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        multiset<int> mset(stones.begin(), stones.end());
        while (mset.size() > 1) {
            auto it1 = mset.end(); it1--;
            auto it2 = it1; it2--;
            int x = *it1; mset.erase(it1);
            int y = *it2; mset.erase(it2);
            if (x != y) {
                mset.insert(x - y);
            }
        }
        return mset.empty() ? 0 : *mset.begin();
    }
};