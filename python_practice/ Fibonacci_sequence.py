nterms = int(input("how many terms"))

n1 ,n2 = 0, 1
count = 0

if nterms <= 0:
    print("Enter the positive no")
elif nterms == 1:
    print("Fibonacci sequence no is ", nterms, ":")
    print(n1)

else:
    print("febonacci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth

        count += 1