from pandas import DataFrame

def parseInput(filename):
    df = DataFrame.read_csv(filename)
    return df
