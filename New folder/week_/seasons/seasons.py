import inflect
from datetime import date
import operator
import sys


p = inflect.engine()

def main():
    try:
        tday = date.today()
        bday = date.fromisoformat(input("Date of Birth: "))
        difference = operator.__sub__(tday, bday)
        operator.sub(tday, bday)
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
