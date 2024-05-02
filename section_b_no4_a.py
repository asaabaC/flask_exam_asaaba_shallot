def calculate_bonus(salary, years_of_service):
    if years_of_service > 4:
        bonus = salary * 0.08
    elif years_of_service == 3:
        bonus = salary * 0.05
    else:
        bonus = 0
    net_salary = salary + bonus
    return bonus, net_salary

while True:
    salary = float(input("Please enter your salary: "))
    years_of_service = int(input("Please enter your years of service: "))
    bonus, net_salary = calculate_bonus(salary, years_of_service)
    print(f"Your net bonus amount is: {bonus}")
    print(f"Your net salary amount is: {net_salary}")
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break
    
    
    
    


if __name__ == "__main__":
    main() # type: ignore
