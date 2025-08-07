'''
Purpose : To show users their monthly and annual pay along with their deductions based on the benefits they have chosen
Programmer : John Kevin R. De Chavez, Jan Lester Nevalga, Warren Jay Rubico
Language : Python
Date Created : 11/03/2022
Date Modified : 11/03/2022
'''

import module

yearly_pay, age = module.employee_info()
health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance = module.optional_benefits(yearly_pay, age)
taxes, monthly_taxes, retirement, monthly_retirement = module.mandatory_deductions(yearly_pay)
annual_totalDeduction, monthly_totalDeduction, monthly_pay, annual_netPay, monthly_netPay = module.total_computations(health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance, taxes, monthly_taxes, retirement, monthly_retirement, yearly_pay)
module.display(health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance, taxes, monthly_taxes, retirement, monthly_retirement, annual_totalDeduction, monthly_totalDeduction, monthly_pay, yearly_pay, annual_netPay, monthly_netPay)


def employee_info():
    print("Welcome to WaLeNJo Co.! \nThis is the Payroll Office's benefits calculator.")
    yearly_pay = float(input("What is your annual gross pay? (Do not use commas.)\n"))
    age = int(input("What is your age?\n"))
    return yearly_pay, age
    
def optional_benefits(yearly_pay, age):
    print('''\nWhich Health Insurance option would you like to choose?
(1) Insurance coverage for self only for $1500.00 per year
(2) Insurance coverage for self and family for $2750.00 per year
Type "1" for choice number one or type "2" for choice number two. Only the two options above are available.''')
    health_insuranceType = int(input())
    if health_insuranceType == 1: 
        health_insurance = 1500
    elif health_insuranceType == 2: 
        health_insurance = 2750
    else:
        print("Invalid option")
    monthly_healthInsurance = health_insurance/12
    ### health_insurance is valid as the annual total health insurance
    ### end of health insurance
    
    disability_insuranceType = input("\nWould you like to have a Disability Insurance? (Yes or No only).\n").lower()
    if disability_insuranceType == "yes":
        disability_insurance = yearly_pay * 0.012
    elif disability_insuranceType == "no":
        disability_insurance = 0
    else:
        print("Invalid option.")
    monthly_disabilityInsurance = disability_insurance/12
    ### disability_insurance is valid as the annual total disability insurance
    ### end of disability insurance
    
    life_insuranceType = input("\nWould you like to have a Life Insurance? (Yes or No only).\n").lower()
    if life_insuranceType == "yes":
        specify_increment = int(input('''Please specify the amount of life insurance that you want.
Each value of 1 is equivalent to $10,000. (e.g., If you input 5, it is equivalent to $50,000).
You can only input whole numbers.\n'''))
        increment = specify_increment * 10000
        life_insurance = (increment/10000) * (25 + (0.95 * (age - 25)))
    elif life_insuranceType == "no":
        life_insurance = 0
    else:
        print("Invalid option.")
    monthly_lifeInsurance = life_insurance/12
    ### life_insurance is valid as the annual total life insurance
    ### end of life insurance
    
    return health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance

def mandatory_deductions(yearly_pay):
    if yearly_pay <= 42000:
        taxes = yearly_pay * 0.18
    else:
        taxes = yearly_pay * 0.28
    monthly_taxes = taxes/12
    
    retirement = yearly_pay * 0.055
    monthly_retirement = retirement/12
    
    return taxes, monthly_taxes, retirement, monthly_retirement
    
def total_computations(health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance, taxes, monthly_taxes, retirement, monthly_retirement, yearly_pay):
    annual_totalDeduction = health_insurance + disability_insurance + life_insurance + taxes + retirement
    monthly_totalDeduction = monthly_healthInsurance + monthly_disabilityInsurance + monthly_lifeInsurance + monthly_taxes + monthly_retirement
    monthly_pay = yearly_pay/12
    annual_netPay = yearly_pay - annual_totalDeduction
    monthly_netPay = monthly_pay - monthly_totalDeduction
    
    return annual_totalDeduction, monthly_totalDeduction, monthly_pay, annual_netPay, monthly_netPay
    
def display(health_insurance, monthly_healthInsurance, disability_insurance, monthly_disabilityInsurance, life_insurance, monthly_lifeInsurance, taxes, monthly_taxes, retirement, monthly_retirement, annual_totalDeduction, monthly_totalDeduction, monthly_pay, yearly_pay, annual_netPay, monthly_netPay):
    print(f''' 
-------------------------------------------------------------------------
                                Annual                    Monthly
-------------------------------------------------------------------------
Deductions:                  
  Health Insurance:         {health_insurance:10.2f}$ {monthly_healthInsurance:24.2f}$
  Disability Insurance:     {disability_insurance:10.2f}$ {monthly_disabilityInsurance:24.2f}$
  Life Insurance:           {life_insurance:10.2f}$ {monthly_lifeInsurance:24.2f}$

  Taxes:                    {taxes:10.2f}$ {monthly_taxes:24.2f}$
  Retirement:               {retirement:10.2f}$ {monthly_retirement:24.2f}$

Gross Pay:                  {yearly_pay:10.2f}$ {monthly_pay:24.2f}$
Total Deductions:           {annual_totalDeduction:10.2f}$ {monthly_totalDeduction:24.2f}$
                            -------------              ------------
Net Pay:                    {annual_netPay:10.2f}$ {monthly_netPay:24.2f}$
    
    ''')
    
        