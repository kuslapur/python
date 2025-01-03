x = int(input("enter no "))

previous_no = 0

for i in range(x,10):
    y = i + previous_no

    previous_no = i

    print(previous_no)

    print(y, end=" ")