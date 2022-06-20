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
    vector<int> preorder;
    
    void preorderTraverse(TreeNode *cur) {
        if (cur == nullptr) return;
        this->preorder.push_back(cur->val);
        preorderTraverse(cur->left);
        preorderTraverse(cur->right);
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        if (root != nullptr) preorderTraverse(root);
        return this->preorder;
    }
};