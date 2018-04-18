from ds.table import Table
from ds.tree import Tree
from ds.header_table import HeaderTable
from pptree import print_tree
from collections import defaultdict,Counter
class FPTree(Tree):

    def __init__(self,dataframe, min_support):
        super().__init__()
        self.df = dataframe
        self.min_support = min_support
        support_table = self.df.value_counts()
        filtered_table = {k:v for k,v in support_table.items() if v >= self.min_support}
        filtered_table = dict(sorted(filtered_table.items(),key=lambda x:x[1], reverse=True))
        filtered_values = list(filtered_table.keys())
        header_table = self.df.row_store
        for idx,row in enumerate(header_table):
            new_row = list(filter(lambda x: x in filtered_values, row))
            new_row.sort(key=lambda x: filtered_values.index(x))
            # new_row = self.sort_row(filtered_table,row)
            header_table[idx] = new_row
        self.header = header_table
        self.sorted = filtered_table
        self.conditional_pattern_base = []
        self.header_table = HeaderTable()
        for row in header_table:
            row_tree = Tree()
            head = row_tree
            for value in row:
                node = Tree(value,1)
                row_tree = row_tree.addChild(node)
            self.mergeTree(head,self.header_table)

    # def constructHeaderTable(self,sorted):


    def performFPGrowth(self, growth_item=[]):
        if self.isSinglePath():
            patterns = {}
            nodes = self.getAllNodes()
            min_support = min([self.sorted[x] for x in nodes])
            for i in range(1, len(nodes)+1):
                for pattern in itertools.combination(nodes, i):
                    # if item is not None:
                    #     pattern += item
                    patterns[tuple(pattern)] = min_support
            # if item is not None:
            #     patterns[tuple(item)] = min_support
            return patterns
        else:
            mine_order = reversed(list(self.sorted.keys()))
            patterns = []
            for item in mine_order:
                suffixes = []
                patterns.append(item)
                patterns.extend(growth_item)
                conditional_pattern_base = []
                node = self.header_table[item]
                while node is not None:
                    suffixes.append(node.value)
                    node = node.link
                for suffix in suffixes:
                    frequency = suffix.support
                    parent = suffix.parent
                    path = []
                    while parent.parent is not None:
                        path.append(parent.item)
                        parent = parent.parent
                    for i in range(frequency):
                        conditional_pattern_base.append(path)
                    self.conditional_pattern_base = conditional_pattern_base
                    #Removing items based on thresold before creating tree
                    #Generating Conditional Pattern Tree here..
                print(conditional_pattern_base)
                conditional_helper = Counter()
                for cond in conditional_pattern_base:
                    for val in cond:
                        conditional_helper[val] += 1
                print(conditional_helper)
                # conditional_pattern_base = [x for x in list(map(lambda x: \
                #                            list(filter(lambda y: conditional_helper[y] > self.min_support, x)),conditional_pattern_base))\
                #                            if x != []]
                for i in range(len(conditional_pattern_base)):
                    cpb = conditional_pattern_base.pop(0)
                    cpb = list(filter(lambda x: conditional_helper[x] >= self.min_support, cpb))
                    if cpb != []:
                        conditional_pattern_base.append(cpb)

                print(list(conditional_pattern_base), )
                conditional_tree = FPTree()
                head = Tree()
                for cpb in conditional_pattern_base:
                    single_tree = Tree()
                    head = single_tree
                    node = Tree(cpb)
                    single_tree = single_tree.addChild(node)
                conditional_tree.mergeTree(head)

                if conditional_tree.item is not None:
                    conditional_tree.performFPGrowth()


                # for item in self.filtered_values:



    # def sort_row(self, filtered_table, row):
    #     filter_group = defaultdict(list)
    #     new_row = []
    #     for k,v in filtered_table.items():
    #         filter_group[v].append(k)
    #     for key,value in sorted(filter_group.items(), key=lambda x:x[0], reverse=True):
    #         for row_val in row:
    #             if row_val in value:
    #                 new_row.append(row_val)
    #     print(filter_group)
    #     return new_row
