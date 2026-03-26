n = int(input("Enter an integer: "))

# Step 1: Find sum of digits
digit_sum = 0
temp = n

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

# Step 2: Check if sum is palindrome
sum_str = str(digit_sum)

if sum_str == sum_str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")