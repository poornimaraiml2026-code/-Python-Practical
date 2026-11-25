import pandas as pd
n = int(input("Enter number of students: "))
names = []
departments = []
attendance = []
marks = []
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    att = input("Enter Attendance (leave blank if missing): ")
    mark = input("Enter Mark (leave blank if missing): ")

    names.append(name)
    departments.append(dept)

    attendance.append(float(att) if att else None)
    marks.append(float(mark) if mark else None)
data = {
    "Name": names,
    "Department": departments,
    "Attendance": attendance,
    "Mark": marks
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

# Descriptive Statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Department-wise Average Marks
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

# EDA Summary
print("\n--- EDA Summary ---")

print("Highest Mark:", df["Mark"].max())
print("Lowest Mark:", df["Mark"].min())
print("Average Mark:", round(df["Mark"].mean(), 2))
print("Average Attendance:", round(df["Attendance"].mean(), 2))

print("\nProgram Completed Successfully!")