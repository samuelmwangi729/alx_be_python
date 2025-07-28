from arithmetic_operations import perform_operation

def main():
    #get the number from the user
    num1 = float(input("enter the number 1\n"))
    num2 = float(input("enter the number 2\n"))
    operation = str(input("enter the operation")).strip().lower()
    result:float = perform_operation(num1,num2,operation)
    print(f"the operation is {result}")

if __name__ =="__main__":
    main()