# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150 
class Node: 
    def __init__(self, ch, is_leaf, child):
        self.ch = ch 
        self.is_leaf = is_leaf
        self.child = child 

    # def __repr__(self):
    #     return 'Node({}, {}, {})'.format(self.ch, self.is_leaf, self.child)
    
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Tree Construction  
        tree = Node(None, False, {})
        for word in wordDict: 
            node = tree
            for ch in word: 
                if ch in node.child: 
                    node = node.child[ch]
                else: 
                    new_node = Node(ch, False, {})
                    node.child[ch] = new_node
                    node = new_node 
            node.is_leaf = True 

        # print(tree)
        # Checking word availability in the tree
        popped = [0] * len(s)
        result = [None] * len(s)
        stack = []
        node = tree 
        ind = 0
        while ind < len(s): 
            ch = s[ind]
            # print(ind, ch)
            if ch in node.child: 
                # print('debug: 1')
                node = node.child[ch]
                if node.is_leaf: 
                    result[ind] = node 
                    stack.append((ind, node))
                # else: 
                #     result[ind] = None
            else: 
                # print('debug: 3')
                if len(stack) == 0: 
                    break 
                else:
                    ind, _ = stack.pop()
                    popped[ind] += 1
                    node = tree  
                    if popped[ind] > 1: break

            if ind == (len(s) - 1) and result[-1] == None:
                if len(stack) == 0: 
                    break 
                else:
                    ind, _ = stack.pop()
                    popped[ind] += 1
                    node = tree 
                    if popped[ind] > 1: break
            
            ind += 1 


        # print(result)
        return result[-1] != None

sol = Solution()
sol.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])