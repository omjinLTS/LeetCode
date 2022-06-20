/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorder;
    
    void traverse(TreeNode *cur) {
        if (cur == nullptr) return;
        traverse(cur->left);
        traverse(cur->right);
        this->postorder.push_back(cur->val);
    }
    
    vector<int> postorderTraversal(TreeNode* root) {
        traverse(root);
        return this->postorder;
    }
};