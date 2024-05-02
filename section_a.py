# NO a(i)

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"

def main():
    percentage = float(input("Enter the student's percentage: "))
    if percentage < 0 or percentage > 100:
        print("Invalid percentage. Please enter a value between 0 and 100.")
    else:
        grade = calculate_grade(percentage)
        print("The student's grade is:", grade)

if __name__ == "__main__":
    main()



#part ii
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")


#part b(i)



def calculate_triangle_area(base, height):
    return 0.5 * base * height


base = 2
height = 3

# print area
area = calculate_triangle_area(base, height)
print("Area of the triangle:", area)




#part b(ii)

def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

sample_list = [9, 2, 3, 5, 8]

sum_of_sample_list = sum_list(sample_list)

print(f"The sum of the sample list is: {sum_of_sample_list}")