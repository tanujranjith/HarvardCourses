import sys
import csv

from tabulate import tabulate

lst = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                lst.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(lst, headers="keys", tablefmt="grid"))

2


Reply


Dors Coding School
·

2 replies
Nomad
Nomad
2 months ago
from tabulate import tabulate
import sys

def main():
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        if len(sys.argv) == 2:
            print(csvCheck(lines))
        elif len(sys.argv) > 2:
            raise IndexError
    except FileNotFoundError:
        sys.exit('File does not exist')
    except IndexError:
        if len(sys.argv) > 2:
            sys.exit('Too many command-line arguments')
        elif len(sys.argv) < 2:
            sys.exit('Too few command-line arguments')


def tabulateFile(lines):
    x = []
    for line in lines:
        item = line.rstrip().split(',')
        x.append(item)
    return tabulate(x, headers='firstrow', tablefmt='grid')


def csvCheck(lines):
    prefix, suffix = sys.argv[1].split('.')
    if suffix == 'csv':
        return tabulateFile(lines)
    else:
        sys.exit('Not a CSV file')


if _name_ == '__main__':
    main()