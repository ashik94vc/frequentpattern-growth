class Node(object):

    def __init__(self, item, support):
        self.item = item
        self.support = support

    def __lt__(self,other):
        return self.item < other.item

    def __le__(self,other):
        return self.item <= other.item

    def __eq__(self,other):
        return self.item == other.item

    def __ne__(self,other):
        return self.item != other.item

    def __ge__(self,other):
        return self.item >= other.item

    def __gt__(self,other):
        return self.item > other.item
