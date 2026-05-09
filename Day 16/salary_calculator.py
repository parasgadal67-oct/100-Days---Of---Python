def  salary_calculator(name, basic, allowance=0.2, tax=0.1):
    employee_name = name
    basic_salary = basic
    basic_allowance = basic_salary * allowance
    tax_amount = basic_salary *tax
    net = basic_salary + basic_allowance - tax_amount
    return f"{employee_name}:{basic_salary} + {basic_allowance} - {tax_amount} = {net}"
print(salary_calculator("Paras Gadal",70000))
