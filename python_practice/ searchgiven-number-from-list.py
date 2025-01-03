l1 = [1,2,3,4,5,6,7,8,9,10]

n = int(input("enter no to search "))

for i in l1:
    if i == n:
        print(" number found ")
        break
else:
    print("number not exist ")