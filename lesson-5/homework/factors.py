def factor(num):
    i = 1
    for i in range(i, num+1):
        if num % i == 0:
            print(f"{i} soni {num} ning bo'luvchisi")
            i += 1

def main():
    factor_num = int(input("Enter a positive integer: "))
    factor(factor_num)

if __name__ == "__main__":
    main()
