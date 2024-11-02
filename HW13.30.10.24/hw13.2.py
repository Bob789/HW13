# solution a
#30 student in class, total 103 student, How many full class have?

students = int(30)
total_student = int(103)
full_class = total_student // students
print(f" full class :{full_class}")

total_student = int(input("Enter total students :"))
full_class = total_student // students
print(f" full class :{full_class}")
remain = total_student % students
print(f" remain :{remain}")

# solution b
string_int = 0
while True:
    try:
        string_int = int(input("Enter number between 10-99:"))
        print(string_int)
        if 10 <= string_int <= 99:
            break
        else:
            continue
    except ValueError:
        # Handle the exception
        print('Please enter an integer')

units = string_int % 10
tens = string_int // 10
if units > tens:
    num = (units * 10) + tens
    print(num)
else:
    print(string_int)


