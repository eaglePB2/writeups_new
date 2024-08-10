def even(n):
    return n/2

def odd(n):
    return (n*3)+1

def main():
    n = int(input())
    while n > 1:
        print(str(int(n)), end=' ')
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
    print(int(n))

if __name__ == "__main__":
    main()