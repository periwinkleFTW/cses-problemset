def main():
    n = int(input())

    zeroes = 0

    while n >= 5:
        zeroes += n // 5
        n = n // 5
    
    print(zeroes)


if __name__ == '__main__':
    main()