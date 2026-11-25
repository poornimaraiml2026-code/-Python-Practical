
# Pandas Series and DataFrame

import pandas as pd

n = int(input("Enter number of students: "))

roll_no = []
names = []
departments = []
mark_list = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    r = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))

    roll_no.append(r)
    names.append(name)
    departments.append(dept)
    mark_list.append(mark)

# Create Pandas Series
marks = pd.Series(mark_list, index=names)

print("\n--- Pandas Series ---")
print(marks)

# Create DataFrame
data = {
    "RollNo": roll_no,
    "Name": names,
    "Department": departments,
    "Mark": mark_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

# Calculate Average Mark
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

# Display students scoring above 85
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])