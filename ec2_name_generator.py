import random
import string

# Ask how many names to generate
num_instances = int(input("How many EC2 instance names do you want to generate? "))

# Ask for department name
department = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

# Basic list of valid departments
valid_departments = ["marketing", "accounting", "finops"]

# Check if the department is allowed
if department not in valid_departments:
    print("❌ This department is not authorized to use this Name Generator.")
else:
    print("\n✅ Generating EC2 instance names...\n")
    for _ in range(num_instances):
        # Generate a random 6-character string (letters + numbers)
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        # Combine department with random string
        ec2_name = f"{department}-{random_part}"
        print(ec2_name)
