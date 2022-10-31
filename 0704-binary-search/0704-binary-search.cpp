class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        int m = 0;
        while (l <= r) {
            m  = (l+r)/2;
            if (nums[m] < target) l = m+1;
            else if (target < nums[m]) r = m-1;
            else return m;
        }
        return -1;
    }
};