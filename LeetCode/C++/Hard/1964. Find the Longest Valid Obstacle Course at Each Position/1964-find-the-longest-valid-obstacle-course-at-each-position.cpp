class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        map<int, int, greater<int>> treeMap;
        vector<int> result(n);
        for (int i = 0; i < n; i++) {
            int h = obstacles[i];
            auto it = treeMap.lower_bound(h);
            if (it != treeMap.end()) {
                int len = it->second + 1;
                treeMap[h] = len;
                // maintain monotonic
                auto it2 = treeMap.find(h);
                if (it2 != treeMap.begin()) {
                    it2 = prev(it2);
                    while (it2 != treeMap.begin()) {
                        auto next = prev(it2);
                        if (it2->second < len) {
                            treeMap.erase(it2);
                        } else {
                            break;
                        }
                        it2 = next;
                    }
                    if (it2->second <= len) {
                        treeMap.erase(it2);
                    }
                }
            } else {
                treeMap[h] = 1;
            }
            result[i] = treeMap[h];
        }
        return result;
    }
};