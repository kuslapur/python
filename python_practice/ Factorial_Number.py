num = int(input("enter number"))

if num < 0:
    print(" entered number is negative ")
elif num == 1:
    print("factorial of 1 is 1 ")
else:
    factorial = 1
    for i in range(1, num+1):
        print(i)
        factorial = factorial * i

    print(f"factorial of {num} is {factorial}")