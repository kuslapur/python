str1 = input("enter the string to compare ")

str2 = "wellsfargo"

len1 = len(str1)
len2 = len(str2)

if len1 == len2:
    for i in range(1, len1):
        if str1[i] == str2[i]:
            print(" equal ")
        else:
            print(" Not equal ")
else:
    print("lenth is not equal")
