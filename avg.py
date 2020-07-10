number = int(input("How many numbers? "))
total_sum = 0
for n in range (number):
    numbers = float(input("Enter any number "))
    total_sum += numbers
avg = total_sum / number
print("Average is : ", avg)