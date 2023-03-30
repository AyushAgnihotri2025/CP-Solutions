class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() < nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int low = 0;
        int high = nums2.size() * 2;
        while (low <= high) {
            int midTwo = (low + high) / 2;
            int midOne = nums1.size() + nums2.size() - midTwo;
            double leftOne = (midOne == 0) ? INT_MIN : nums1[(midOne - 1) / 2];	
            double leftTwo = (midTwo == 0) ? INT_MIN : nums2[(midTwo - 1) / 2];
            double rightOne = (midOne == nums1.size() * 2) ? INT_MAX : nums1[(midOne) / 2];
            double rightTwo = (midTwo == nums2.size() * 2) ? INT_MAX : nums2[(midTwo) / 2];
            if (leftOne > rightTwo) {
                low = midTwo + 1;
            } else if (leftTwo > rightOne) {
                high = midTwo - 1;
            } else {
                return (max(leftOne, leftTwo) + min(rightOne, rightTwo)) / 2;	
            }
        }
        return -1;
    }
};