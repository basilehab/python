import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    m = re.findall(r"\bum\b", s, re.IGNORECASE)
    counter = m.count("um")
    return counter


if __name__ == "__main__":
    main()
