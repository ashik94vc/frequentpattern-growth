class Node(object):
    def __init__(self, value, link):
        assert isinstance(link,Node) or link is None
        self.link = link
        self.value = value

    def append(self,new_node):
        node = self
        while node.link is not None:
            node = node.link
        node.link = new_node

    def modify(self,new_node,child):
        node = self
        while node.link is not None:
            if node.value == new_node.value:
                node.value.support += 1
                break
            node = node.link

    def __str__(self):
        pattern = "({0!s}:{0!s})->"
        if self.value is not None:
            rpr = "("+str(self.value.item)+":"+str(self.value.support)+")->"
            rpr += str(self.link)
        else:
            rpr = "(None)"
        return rpr

class HeaderTable(object):

    def __init__(self):
        self.table = {}

    def addEntry(self, item, node):
        self.table[item] = node

    def getEntry(self, item):
        return self.table[item]

    def __iter__(self):
        return iter(self.table.keys())

    def __repr__(self):
        pattern = "{} :: {}\n"
        rpr = ""
        for key,value in self.table.items():
            rpr += str(key)+" :: "+str(value)+"\n"
        return rpr

    def __getitem__(self, item):
        return self.table[item]

    def __setitem__(self, item, node):
        self.table[item] = node
