"""
n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Blastoff!")

#Assignment
hrs = input("Enter Hours:")
rph = input("Enter Rate :")


hrs = float(hrs)
rph = float(rph)

gross_pay = hrs * rph
print("Pay:", gross_pay)


#Puzzle: Which will never print regardless of the value for x ? else :
    print("Something else"), elif x < 10 :
    print("Below 10")

A) if x < 2 :                       
    print("Below 2")                     
elif x >= 2 :
    print("Two or more")
else :
    print("Something else")

B) if x < 2 :
    print("Below 2")
elif x < 20 :
    print("Below 20")
elif x < 10 :
    print("Below 10")
else : 
    print("Something else")

#Assignment
hrs = input("Enter Hours:")
rph = input("Enter Rate:")

hrs = float(hrs)
rph = float(rph)

gross_pay = rph * hrs
if hrs > 40 :
    print(hrs * 1.5)

#Right Answer
# Prompt the user for hours worked and hourly rate
hours_str = input("Enter hours worked: ")
rate_str = input("Enter hourly rate: ")

# Convert the input strings to numbers
hours = float(hours_str)
rate = float(rate_str)

# Calculate the gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * 1.5 * rate
    gross_pay = regular_pay + overtime_pay

# Display the gross pay
print("Gross pay: $", gross_pay)

#Practice
#1)
salary = input("What is your salary:")
yoe = input("How many years of service")

yoe = float(yoe)
salary = float(salary)

if yoe >= 5:
    print("You will receive 5% more!")
else :
    print("You are ineligible for this reward")


#assignment
score = input("Enter Score: ")

if score >= 0.9:
    print("A")
"""
print("Hello World")
