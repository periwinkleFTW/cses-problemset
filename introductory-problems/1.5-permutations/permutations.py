def main():
    n = int(input())

    if n == 1:
        print(n)
    elif n < 4:
        print('NO SOLUTION')
    else:
        for num in range(2, n+1, 2):
            print(num)
        for num in range(1,n+1,2):
            print(num)
        

if __name__ == '__main__':
    main()