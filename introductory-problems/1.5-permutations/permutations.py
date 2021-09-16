def main():
    n = int(input())

    if n == 1:
        print(n)
    elif n == 2 or n == 3:
        print('NO SOLUTION')
    else:
        a = []
        for num in range(n):
            if num % 2 == 0:
                a.append(num)
        for num in range(n):
            if num % 2 != 0:
                a.append(num)

        print(a)
        

if __name__ == '__main__':
    main()