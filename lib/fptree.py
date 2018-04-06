from pandas import DataFrame

def constructHeader(min_support=0):
    header = df.stack().value_counts().to_frame()
    header = header.drop(header[header[0] < min_support].index)
    order = list(header.T.columns.values)
    return header.T
