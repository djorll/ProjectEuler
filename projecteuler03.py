# version python 3.4
# -*- coding: utf-8 -*-
# décomposition en facteurs premiers

def decompose(n):
    print("%d=1" % (n), end=' ')
    i = 2
    while n > 1:
        while n % i == 0:
            print("x", i, end=' ')
            n = n / i
        i = i + 1
    print("\n")  # saut de ligne


def main():
    decompose(600851475143)


if __name__ == '__main__':
    main()