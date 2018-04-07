from ds import *
from lib import FPTree
import sys
from pptree import print_tree

data = Table().from_csv(sys.argv[1],missing_char="")

fptree = FPTree(data,min_support=3)

print(fptree.header)
print(fptree.sorted)
print_tree(fptree.fptree)
