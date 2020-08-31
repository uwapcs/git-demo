def do_fizzbuzz():
    for i in range(100):
        if (i % 5 == 0):
            print("BUZZ")
        else:
            print(i)


def main():
    do_fizzbuzz()


if __name__ == "__main__":
    main()
