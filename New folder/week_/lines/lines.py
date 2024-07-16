import csv
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a CSV file")
        else:
            countline(sys.argv[1])

def countline(input):
        try:
            counter = 0
            with open(input) as input:
                for line in input:
                    if not (line.lstrip().startswith("#") or line.strip() == ""):
                        counter = counter + 1

            print(counter)
        except FileNotFoundError:
            sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
