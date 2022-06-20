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
    vector<int> inorder;
    
    void inorderTraverse(TreeNode *cur) {
        if (cur == nullptr) return;
        inorderTraverse(cur->left);
        this->inorder.push_back(cur->val);
        inorderTraverse(cur->right);
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        inorderTraverse(root);
        return this->inorder;
    }
};