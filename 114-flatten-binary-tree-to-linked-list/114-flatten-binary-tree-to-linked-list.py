# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def flatten(self, root: Optional[TreeNode]) -> None:

		self.previous_node = None

		def DepthFirstSearch(root):

			if root is None: 
				return None

			DepthFirstSearch(root.right)
			DepthFirstSearch(root.left)

			root.right = self.previous_node
			root.left = None 
			self.previous_node = root

			return root

		DepthFirstSearch(root)

		return root
        