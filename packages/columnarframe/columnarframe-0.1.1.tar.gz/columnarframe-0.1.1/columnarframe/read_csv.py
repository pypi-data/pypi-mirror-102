import csv
from .frame import ColumnarFrame


def read_csv(filename, **kwargs):
    with open(filename) as f:
        csvdata = csv.reader(f, **kwargs)

        rit = iter(csvdata)
        header = next(rit)

        data = {key: [] for key in header}
        for row in rit:
            for key, value in zip(header, row):
                if len(value) == 0:
                    value = None
                data[key].append(value)

    return ColumnarFrame(data)
