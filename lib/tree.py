class Tree(object):

    def __init__(self, node=None, children=list()):
        self.node = None
        self.children = children

    def addChild(self, child):
        assert isinstance(child,Tree), "Child should be of type %r" % type(self)
        self.children.append(child)

    def addChildren(self, children):
        assert isinstance(children, list), "Children should be of type list found %r" % type(children)
        assert all(isinstance(child,Tree) for child in children), "Children should be a list of Tree, found a list of %r" %type(children[0])
        self.children.extend(children)
