p = float(input("enter the princeple amount "))
t = int(input("enter the time period "))
r = float(input("enter the rate of intrest "))

simple_intrest = (p*t*r)/100
print(f"simple intrest {simple_intrest}")

total_due = simple_intrest + p

print(f"total due amount {total_due}")