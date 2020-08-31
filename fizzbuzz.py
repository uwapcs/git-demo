def do_fizzbuzz():
    for i in range(100):
        if (i % 3 == 0):
            print("fizz")
        if (i % 5 == 0):
            print("buzz")
        else:
            print(i)


def main():
    do_fizzbuzz()


if __name__ == "__main__":
    main()
