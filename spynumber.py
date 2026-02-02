# Number to check
num = int(input("Enter a number: "))
temp = num
sum_digits = 0
product_digits = 1

while temp > 0:
    
    # Get last digit
    digit = temp % 10  
    
    # Add digit to sum
    sum_digits += digit  
    
    # Multiply digit to product
    product_digits *= digit  
    
    # Remove last digit
    temp //= 10  

# Check if sum equals product
if sum_digits == product_digits:
    print(f"{num} is a Spy Number")
else:
    print(f"{num} is not a Spy Number")