class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int pre1=cost[0],pre2=cost[1],curr=0;
        int n=cost.size();
        for(int i=2;i<n;i++){
            curr=min(pre1,pre2)+cost[i];
            pre1=pre2;
            pre2=curr;
        }
        return min(pre2,pre1);
    }
};