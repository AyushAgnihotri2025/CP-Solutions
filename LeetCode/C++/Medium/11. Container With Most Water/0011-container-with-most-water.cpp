class Solution {
public:
    int maxArea(vector<int>& height) {
        int N = height.size();
        int left = 0, right = N-1, ans = 0;
        while(left < right){
            ans = max(ans, min(height[left], height[right]) * (right-left));
            if(height[left] < height[right]){
                left++;
            }else{
                right--;
            }
        }
        return ans;
    }
};