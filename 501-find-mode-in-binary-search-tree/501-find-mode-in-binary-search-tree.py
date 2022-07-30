# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        final_mode, max_freq = root.val, 1
        dict_nums = {}
        
        def check_tree(node, dict_nums):
            if not node: return dict_nums
            
            if node.val in dict_nums: dict_nums[node.val] += 1
            else: dict_nums[node.val] = 1
            
            if node.left: check_tree(node.left, dict_nums)
            if node.right: check_tree(node.right, dict_nums)
            
            return dict_nums
            
        check_tree(root, dict_nums)
        max_num = max(dict_nums.values())
        '''
        ans = []
        for i, val in dict_nums.items():
            if val == max_num:
                ans.append(i)
        return ans
        '''
        
        return (i for i,val in dict_nums.items() if(val == max_num))