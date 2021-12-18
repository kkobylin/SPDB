import csv


# Return read data in format (x, y, class) in each row
def read_tsv(path):
    tsv_file = open(path)
    tsv_reader = csv.reader(tsv_file, delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)
    data = list(tsv_reader)

    return data


def read_csv(path):
    csv_file = open(path)
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    data = list(csv_reader)

    return data
