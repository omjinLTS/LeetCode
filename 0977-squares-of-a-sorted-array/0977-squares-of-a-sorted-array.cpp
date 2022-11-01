class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> sorted(n);
        int l = 0, r = n-1, t;
        for (int i = 0; i < n; i++) nums[i] *= nums[i];
        while (l <= r) sorted[--n] = nums[l]<nums[r]?nums[r--]:nums[l++];
        return sorted;
    }
};