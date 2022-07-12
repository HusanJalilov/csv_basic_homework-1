import csv
from posixpath import split
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    print(type(data))
    data1=data.split("\n")
    for x in data1:
        y=str(x)
        z=y.split(",")
        print(z[0])

data=open('data.csv').read()
find_number_of_columns(data)


# Read the csv file