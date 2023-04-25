class SmallestInfiniteSet {
public:
    set<int>A;
    SmallestInfiniteSet() {
        A.clear();
        for( int i = 1 ; i <= 1000 ; i++ )
        A.insert(i);
    }
    int popSmallest() {
        int a = *A.begin() ; A.erase(A.begin());
        return a ;
    }
    void addBack(int num) {
        A.insert(num);
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */