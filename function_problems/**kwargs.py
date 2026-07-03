def employee_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
employee_details(Name="Jegan",Age=25,Department="AI",Salary=50000)