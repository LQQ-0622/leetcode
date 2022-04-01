# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree1(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root

    def buildTree11(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def myBuildTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right: return None
            pre_root = pre_left
            in_root = in_root_index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            left_sub_tree_len = in_root - in_left
            root.left = myBuildTree(pre_left + 1, pre_left + left_sub_tree_len, in_left, in_root - 1)
            root.right = myBuildTree(pre_left + left_sub_tree_len + 1, pre_right, in_root + 1, in_right)
            return root

        in_root_index = {val: index for index, val in enumerate(inorder)}
        return myBuildTree(0, len(preorder) - 1, 0, len(preorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
result = Solution().buildTree1(preorder, inorder)
print(result)
