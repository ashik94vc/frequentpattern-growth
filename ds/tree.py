from ds.header_table import Node
from pptree import print_tree
class Tree(object):

    def __init__(self, item=None, support=None):
        self.item = item
        self.support = support
        self.parent = None
        self.children = []

    def __contains__(self,other):
        for child in self.getChildren():
            if child == other:
                return True
        return False

    def __repr__(self):
        return str(self.item)+":"+str(self.support)

    # def __repr__(self, level=0):
    #     ret = "\t"*level+str(self.item)+"\n"
    #     for child in self.children:
    #         ret += child.__repr__(level+1)
    #     return ret

    @property
    def value(self):
        return (self.item,self.support)

    def __hash__(self):
        return hash(self.item)

    def __eq__(self, other):
        assert isinstance(other,Tree), "Can only compare with objects of same type"
        if other.item == self.item:
            return True
        else:
            return False

    def isLeafNode(self):
        if len(self.children) == 0:
            return True
        return False

    def addChild(self, child):
        assert isinstance(child,Tree), "Child should be of type %r" % type(self)
        child.parent = self
        self.children.append(child)
        return self.children[-1]

    def getChildren(self):
        return self.children

    def getChild(self,childIndex):
        return self.children[childIndex]

    def addChildren(self, children):
        assert isinstance(children, list), "Children should be of type list found %r" % type(children)
        assert all(isinstance(child,Tree) for child in children), "Children should be a list of Tree, found a list of %r" %type(children[0])
        for child in children:
            child.parent = self
        self.children.extend(children)

    def childIndex(self, child):
        for idx,chi in enumerate(self.children):
            if chi == child:
                return idx
        return -1

    def getAllNodes(self,aslink=False):
        assert self.isSinglePath(), "Works only for single path trees"
        tree = self
        nodes = []
        while not tree.isLeafNode():
            if tree.item is not None:
                if aslink:
                    nodes.append(tree)
                else:
                    nodes.append((tree.item, tree.support))
            tree = tree.children[0]
        if aslink:
            nodes.append(tree)
        else:
            nodes.append((tree.item, tree.support))
        return nodes

    def isSinglePath(self):
        if self.isLeafNode():
            return True
        if len(self.children) > 1:
            return False
        return self.children[0].isSinglePath()

    #Prunes tree by removing items which have support less than the thresold
    def pruneTree(self, thresold):
        #TODO: Implement this method
        #NOTE: The tree is present in self. You can find the childrens of tree using self.children
        #NOTE: self.children returns a list of tree nodes and it's recursive
        children = self.children
        idx = 0
        while idx < len(children):
            child = children[idx]
            if child.support < thresold:
                children.extend(child.children)
                children.remove(child)
            idx += 1

    def mergeTree(self, tree, header_table=None,recur=False):
        if self == tree:
            for child in tree.children:
                if child in self:
                    id = self.childIndex(child)
                    self_child = self.getChild(id)
                    if header_table is not None:
                        if child.item not in header_table:
                            header_table[child.item] = Node(child, None)
                        else:
                            header_table[child.item].modify(Node(self_child,None),child)
                    self_child.support += child.support
                    self_child.mergeTree(child,header_table,recur=True)
                else:
                    if header_table is not None:
                        node = tree
                        nodes = tree.getAllNodes(aslink=True)
                        if recur:
                            nodes.pop(0)
                        for node in nodes:
                            if node.item not in header_table:
                                header_table[node.item] = Node(node, None)
                            else:
                                header_table[node.item].append(Node(node,None))
                    self.addChild(child)
