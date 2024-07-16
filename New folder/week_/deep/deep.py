def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if scope(x) == "42" or scope(x) == "forty-two" or scope(x) == "forty two":
        print ("yes")
    else:
        print ("no")
def     scope(x):
    x=x.strip().casefold()
    return (x)
main()

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

right = ["42", "forty two", "forty-two"]

if answer in right:
    print("Yes")
else:
    print("No")
