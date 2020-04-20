import datetime
# Create two companies, and 5 people 
# who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a 
# business name, and its employees.

class Employee:
    def __init__(self, first_name, last_name, job, date):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.start_date = date
        
class Company:
    def __init__(self, name, address, industry_type):
        self.business_name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
        
dollar_general = Company("Dollar General", "102 Rivergate Pkwy, Goodletsville, Tn", "Grocery and Supplies")
tesla = Company("Tesla", "778 Richmond Drive", "Automotive Innovation")

Adrian = Employee("Adrian", "Reeds", dollar_general, datetime.datetime.now().date())
Kristen = Employee("Kristen", "Reeds", dollar_general, datetime.datetime.now().date())
Savannah = Employee("Savannah", "Reeds", tesla, datetime.datetime.now().date())
Andrea = Employee("Andrea", "Reeds", tesla, datetime.datetime.now().date())
Tom = Employee("Tom", "Reeds", tesla, datetime.datetime.now().date())

dollar_general.employees.append(Adrian)
dollar_general.employees.append(Kristen)
tesla.employees.append(Savannah)
tesla.employees.append(Andrea)
tesla.employees.append(Tom)

print(f"{dollar_general.business_name} is in the {dollar_general.industry_type} industry and has the following employees:")
for employee in dollar_general.employees:
    print(f"*{employee.first_name} {employee.last_name}")
    
print(f"{tesla.business_name} is in the {tesla.industry_type} industry and has the following employees:")
for employee in tesla.employees:
    print(f"*{employee.first_name} {employee.last_name}")
