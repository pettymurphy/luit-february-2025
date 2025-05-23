import random
import string

def generate_ec2_names():
    num_instances = int(input("How many EC2 instance names do you want to generate? "))
    department = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    valid_departments = ["marketing", "accounting", "finops"]

    if department not in valid_departments:
        print("❌ This department is not authorized to use this Name Generator.")
        return  # Stop the function if invalid department

    print("\n✅ Generating EC2 instance names...\n")
    for _ in range(num_instances):
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        ec2_name = f"{department}-{random_part}"
        print(ec2_name)

# Call the function to run the script
generate_ec2_names()
