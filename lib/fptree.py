from lib.node import Node
from lib.table import Table
from lib.tree import Tree

class FPtree(object):

    def __init__(self,dataframe, min_support):
        self.df = dataframe
        self.min_support = min_support
        support_table = self.df.value_counts()
        filtered_table = {k:v for k,v in support_table.items() if v > self.min_support}
        filtered_table = dict(sorted(filtered_table.items(),key=lambda x:x[1], reverse=True))
        filtered_values = list(filtered_table.keys())
        header_table = self.df.row_store
        for idx,row in enumerate(header_table):
            new_row = list(filter(lambda x: x in filtered_values, row))
            new_row = new_row.sort(key=lambda x: filtered_values.index(x))
            header_table[idx] = new_row

        self.fptree = Tree()

        for row in header_table:
            row_tree = Tree()
            for value in row:
                node = Tree(Node(value, 1))
                row_tree = row_tree.addChild(node)
            self.fptree.mergeTree(row_tree)
