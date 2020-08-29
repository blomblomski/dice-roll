from random_number_generator import random_number, random_numbers


def main():
    x = ' '
    print('exit to exit,', 'n for new random numbers')
    while x != 'exit':
        x = input()
        if x == 'n':
            print(random_numbers(2))


if __name__ == "__main__":
    main()
