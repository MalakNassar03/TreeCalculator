#the Data
A=[3,20,1,4,0]

P = [
    ('x1', 'x3', '+', 'v1'),
    ('x2', 'v1', '*', 'x4'),
    ('x3', 'x6', '-', 'x5'),
    ('x4', 'v3', '+', 'v4'),
    ('x5', 'v2', '*', 'x4'),
    ('x6', 'v5', '-', 'v2'),
    ('x7', 'x1', '-', 'x2'),
]


class Node:
    def __init__(self,val=0,right=None,left=None,operand=None):
        self.val=val
        self.right=right
        self.left=left
        self.operand=operand

def build_tree(P):
    x_nodes = {}# the idea used here is to get all the x nodes and store them in a dict for faster lookup and to find the nodes when wiring.

    #X4=v3+v4
    # first iteration: we create all the Xs with its operand to keep the wiring in the second loop
    for (node, left_op, op, right_op) in P:
        x_nodes[node] = Node(val=node,operand=op)

    # second itereation: to wire stuff up for example we have x1 = x3 + v1, the node already has the operand the value is null
    #
    for (node, left_op, op, right_op) in P:
        node = x_nodes[node]# X1 we get the node to start wiring
        # left child X3 if its in the Xs nodes so its the nodeX which is X then get it else its a V then create the node V=>Node(val=left_op)
        # for V now its a node with no operand
        node.left = x_nodes.get(left_op, Node(val=left_op))
        # right child V1 if its in teh Xs nodes so its nodeX which is X then get it else its a V then create the node V=>Node(val=right_op)
        node.right = x_nodes.get(right_op, Node(val=right_op))

    return x_nodes[P[-1][0]]  #[-1] last tuple  (it represents the last value ) which is X7 which is teh root


def CalculatorTree(P,A):
    root = build_tree(P)

    def dfs(node):
        if not node:
            return None
        # we find the leaf node and start calculating and propegating to the parent
        # okay so for the leaf node i created a variable val, all leaf nodes are technically V
        if not node.right and not node.left:
            val=node.val
            if val.startswith('v'):# in the node its stored a Value starting with V so we can idenify it(making sure its v)
                return A[int(val[1:])-1] # get the number so we can get the index of arr

        #dfs reach the depth
        left=dfs(node.left)
        right=dfs(node.right)

        #if right and left where found(both not null) then we can compute a value

        if right is not None and left is not None:
            if node.operand =="+":
                return left+right
            elif node.operand =="*":
                return left * right
            elif node.operand =="-":
                return left - right
            return None
        return None

    return dfs(root)# return the value from computing





print(CalculatorTree(P,A)) # here i tested my code














