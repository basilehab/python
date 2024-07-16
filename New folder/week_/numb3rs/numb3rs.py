import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        first = matches.group(1)
        sec = matches.group(2)
        third = matches.group(3)
        forth = matches.group(4)
        if (int(first)) <= 255 and (int(sec)) <= 255 and (int(third)) <= 255 and (int(forth)) <= 255:
            return True
        elif (int(first)) > 255 or (int(sec)) > 255 or (int(third)) > 255 or (int(forth)) > 255:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
