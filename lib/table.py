import csv
from collections import defaultdict

class Table(object):
# Structure as Map of Map {colname: [row_index] }
    def __init__(self, array=None):
        if array is not None:
            self.store = {str(i):x for i,x in enumerate(list(map(list, zip(*array))))}
        else:
            self.store = defaultdict(list)

    @property
    def column_store(self):
        return list(self.store.values())

    @property
    def column_header(self):
        return list(self.store.keys())

    @property
    def row_store(self):
        return list(map(list, zip(*self.column_store)))

    def __getitem__(self,key):
        return self.row_store[key]

    def __getattr__(self,key):
        return self.store[key]

    def __repr__(self):
        rep_mat = [self.column_header] +[" "]*len(self.column_header)+ self.row_store
        rep_str = "\tTable\t"
        for row in rep_mat:
            rep_str = rep_str + "\n" + "\t".join(map(str,row))
        return rep_str

    def loc(self,key):
        return self.column_store[key]

    def drop(self,key):
        if key in self.store:
            del self.store[key]

    def from_csv(self, csv_file, has_header=False, missing_char = '?'):
        csvfile = open(csv_file, newline='')
        csvreader = csv.reader(csvfile)
        header = list()
        if has_header:
            header = csvreader.next()
        for row in csvreader:
            row = [x if x != missing_char else None for x in row]
            header = [str(x) for x in range(len(row))]
            for idx,val in enumerate(row):
                self.store[header[idx]].append(val)
