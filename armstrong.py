num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

armstrong_sum = sum(int(d)**power for d in digits)

if armstrong_sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
