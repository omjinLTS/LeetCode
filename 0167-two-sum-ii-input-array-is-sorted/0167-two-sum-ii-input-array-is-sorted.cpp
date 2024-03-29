class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size()-1, s;
        vector<int> result(2);
        while (1) {
            s = numbers[l]+numbers[r];
            if (s < target) l++;
            else if (s > target) r--;
            else {
                result[0] = l+1, result[1] = r+1;
                return result;
            }
        }
    }
};