from sum_module import add
from diff_module import subtract

def main():
    a = int(input("enter the first number :"))
    b = int(input("enter the second number :"))
    print("sum :",add(a,b))
    print("difference :",subtract(a,b))

if __name__ == "__main__":
    main()