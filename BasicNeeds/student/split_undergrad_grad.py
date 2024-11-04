
import pandas as pd

# Load the CSV file
input_file = 'data/student/statewide_student_23.csv'  

# Read the CSV file into a DataFrame
data = pd.read_csv(input_file, low_memory=False)

# Define the student roles we want to keep
student_roles = [
    'Undergraduate student (Part-time, less than 12 credit hours)',
    'Undergraduate student (Full-time, 12 credit hours or more)',
    'Graduate or professional student',
]

# Filter to keep ONLY these student roles for student data
student_data = data[data['Type'].isin(student_roles)]

# Get non-student data
non_student_data = data[~data['Type'].isin(student_roles)]

# Count all types including non-student roles
all_type_counts = data['Type'].value_counts()

# Count student responses
total_students = len(student_data)
undergrad_ft_count = len(student_data[student_data['Type'] == 'Undergraduate student (Full-time, 12 credit hours or more)'])
undergrad_pt_count = len(student_data[student_data['Type'] == 'Undergraduate student (Part-time, less than 12 credit hours)'])
grad_count = len(student_data[student_data['Type'] == 'Graduate or professional student'])

print("\nComplete breakdown of all types in dataset:")
print("-------------------------------------------")
for type_name, count in all_type_counts.items():
    print(f"{type_name}: {count}")

print("\nSummary:")
print("--------")
print(f"Total students: {total_students}")
print(f"- Full-time undergrad students: {undergrad_ft_count}")
print(f"- Part-time undergrad students: {undergrad_pt_count}")
print(f"- Graduate students: {grad_count}")
print(f"\nTotal non-student responses: {len(non_student_data)}")