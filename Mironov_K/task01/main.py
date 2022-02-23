
import sys


DICTIONARY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "


def caesar_cipher(str_work: str, int_key: int) -> str:
    list_result = []
    for item in str_work:
        int_index = (DICTIONARY.find(item) + int_key) % len(DICTIONARY)
        list_result.append(DICTIONARY[int_index])
    return "".join(list_result)


def main(args: list):
    int_key = int(args[3])
    if args[1] == 'd':
        int_key *= -1
    elif args[1] != 'e':
        print("Invalid param1")
        sys.exit(-1)
    print(caesar_cipher(args[2], int_key))


if __name__ == '__main__':
    main(sys.argv)

