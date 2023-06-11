class SnapshotArray {
    int currSnapId = 0;
    unordered_map<int, vector<pair<int,int>>> arr;
    int len;
public:
    SnapshotArray(int length) {
        len = length;
    }
    
    void set(int index, int val) {
        if(!arr[index].empty() && arr[index].back().first == currSnapId) {
            arr[index].pop_back();
        }
        arr[index].push_back({currSnapId, val});
    }
    
    int snap() {
        currSnapId++;
        return currSnapId-1;
    }
    
    int get(int index, int snap_id) {
        auto it = lower_bound(arr[index].rbegin(), arr[index].rend(), make_pair(snap_id, INT_MAX), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a > b;
        });
        if(it == arr[index].rend()) return 0;
        else return it->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */