import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = re.search("^(0?[1-9]|1[0-2]):?([0-5][0-9])?[ ](AM|PM)[ ]to[ ](0?[1-9]|1[0-2]):?([0-5][0-9])?[ ](AM|PM)$", s, re.IGNORECASE)
    if s:
        from_time = standardize(s.group(1), s.group(2), s.group(3))
        time = standardize(s.group(4), s.group(5), s.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError


def standardize(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
