from node import Node
class Tree(object):

    def __init__(self, item=None, support=None):
        self.item = item
        self.support = support
        self.parent = None
        self.children = list()

    def __contains__(self,other):
        for child in self.getChildren():
            if child == other:
                return True
        return False

    def __repr__(self, level=0):
        ret = "\t"*level+str(self.item)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def __eq__(self, other):
        assert isinstance(other,Tree), "Can only compare with objects of same type"
        if other.item == self.item:
            return True
        else:
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

    def mergeTree(self, tree):
        if self == tree:
            for child in tree.children:
                if child in self:
                    id = self.childIndex(child)
                    self_child = self.getChild(id)
                    self_child.support += child.support
                    self_child.mergeTree(child)
                else:
                    self.addChild(child)
