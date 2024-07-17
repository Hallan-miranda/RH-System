with open("hr_system.txt") as employees_data:
    for employee in employees_data:
        employee_data = employee.split()
        name = employee_data[0]
        id_number = employee_data[1]
        job_title = employee_data[2]
        salary = employee_data[3]
        print(f"{name} (ID: {id_number}), {job_title} - ${salary}")