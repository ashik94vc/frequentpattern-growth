from ds import *
from lib import FPTree
import sys
from pptree import print_tree
from configparser import ConfigParser

config = ConfigParser()
config.read('config/fpconfig.rc')

default_config = config['DEFAULT']

minimum_support = 10

MIN_SUP_KEY = "minimum_support"

SEP_KEY = "separator"

flag_verbose = False

separator = ","

if MIN_SUP_KEY in default_config:
    minimum_support = int(default_config[MIN_SUP_KEY])

if SEP_KEY in default_config:
    separator = default_config[SEP_KEY].strip('"')

if len(sys.argv) > 3:
    if sys.argv[3].isdigit():
        minimum_support = int(sys.argv[3])
        if len(sys.argv) == 5:
            if sys.argv[4] == "-v":
                flag_verbose = True
    if sys.argv[3] == "-v":
        flag_verbose = True

data = Table().from_csv(sys.argv[1],separator,missing_char="")

fptree = FPTree(data,min_support=minimum_support)

fptree.performFPGrowth()

out_file_name = sys.argv[2]

file = open(out_file_name, "w+")

for pattern in fptree.patterns:
    if flag_verbose:
        print(",".join(pattern))
    file.write(",".join(pattern)+"\n")
file.close()
