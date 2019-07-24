"""
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 比较容易理解的一种思路  递归
class Solution():
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        if root.left:
            root.left.val = root.val + root.left.val
        if root.right:
            root.right.val = root.val + root.right.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
      
      
      
 # 官方解法：递归暴力破解
class Solution():
    def hasPathSum(self, root, sum):

        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
