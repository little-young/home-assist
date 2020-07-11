from collections import OrderedDict

import pyorc


def iter_orc(path):
    with open(path, 'rb') as f:
        reader = pyorc.Reader(f)
        column_names = reader.schema.fields.keys()
        for item in reader:
            d = OrderedDict(zip(column_names, item))
            yield d


