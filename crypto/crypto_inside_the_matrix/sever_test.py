from sage.all_cmdline import *
# from utils import ascii_print
import os

print("Herllo world")

FLAG = b"HTB{????????????????????}"
assert len(FLAG) == 25


class Book:

    def __init__(self):
        self.size = 5
        self.prime = None

    def parse(self, pt: bytes):
        pt = [b for b in pt] # convert to decimal
        print(pt)
        return matrix(GF(self.prime), self.size, self.size, pt)

    def generate(self):
        key = os.urandom(self.size**2)
        return self.parse(key)

    def rotate(self):
        self.prime = random_prime(2**6, False, 2**4)

    def encrypt(self, message: bytes):
        self.rotate()
        print("===============PRINME==============")
        print(self.prime)

        key = self.generate()
        print("===============KEY==============")
        print(key)

        print("===============MESSAGE==============")
        print("Before: " + message.decode('utf-8'))
        message = self.parse(message)
        print(message)
        
        ciphertext1 = message * key
        print("============CIPHER============")
        print(ciphertext1)
        ciphertext2 = key * message
        print("============CIPHER============")
        print(ciphertext2)

        return ciphertext1, ciphertext2, key


def menu(): 
    print("Options:\n")
    print("[L]ook at page")
    print("[T]urn page")
    print("[C]heat\n")
    option = input("> ")
    return option


def main():
    book = Book()
    while True:
        ciphertext1, ciphertext2, key = book.encrypt(FLAG)
        if (ciphertext1 == ciphertext2):
            break
    page_number = 1

    while True:
        option = menu()
        if option == "L":
            # ascii_print(ciphertext, key, page_number)
            print(ciphertext, key, page_number)
        elif option == "T":
            ciphertext, key = book.encrypt(FLAG)
            page_number += 2
        elif option == "C":
            print(f"\n{list(ciphertext)}\n{list(key)}\n")
        else:
            print("\nInvalid option!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
