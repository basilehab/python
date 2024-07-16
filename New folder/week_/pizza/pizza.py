import csv
import sys
#from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1])

def clean(input):
        try:
            with open(input) as input:
                    reader = csv.DictReader(input)
                    table = reader
#                    print(tabulate(table, headers="firstrow", tablefmt="outline"))

        except FileNotFoundError:
            sys.exit(f"Could not read {input}")
#        except reportMissingModuleSource:
#            sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
