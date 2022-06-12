class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int N = cost.size();
        cost.push_back(0);
        for (int i = 2; i <= N; i++) {
            cost[i] += min(cost[i-1], cost[i-2]);
        }
        return cost[N];
    }
};