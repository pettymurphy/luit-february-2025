# luit-february-2025
Demo repository
luit-february-2025

This repository is dedicated to my Python learning journey, starting February 2025.

As I continue developing my skills in Python, this will serve as the central location for:
- All Python scripts I build as part of my class assignments and personal learning
- Experiments and practice projects related to automation, DevOps, and AWS scripting
- Version-controlled development using GitHub

Expect to see beginner to intermediate-level scripts that gradually build up in complexity over time. This will evolve as my skills and confidence in Python improve.

🛠️ Topics will include:
- Input handling and conditionals
- Functions and reusable logic
- Scripting for EC2 and AWS automation
- Security tools, CVE checks, and more

Stay tuned as I continue updating this repo with hands-on code, notes, and progress updates.

# LUIT February 2025 – File Metadata Extraction 
## 📌 Project Overview

This foundational Python script scans the **my current working directory** and creates a list of dictionaries — each containing the **name** and **size** (in bytes) of the files it finds. This serves as the first phase of a data extraction pipeline for identifying file attributes at scale.

---

## 🧠 What It Does

- Loops through all files in the directory where the script is run
- Skips directories (only includes files)
- Collects and returns:
  - `name`: file name (string)
  - `size`: file size in bytes (integer)
- Prints the final list of dictionaries to the console

*Key Script Highlights:**
- Uses `os.listdir()` to list files.
- Uses `os.path.isfile()` to filter out folders.
- Simple and ideal for small-scale, top-level file inspections.

---

## 💻 How to Run

Make sure you have Python 3 installed.

```bash
python list_files.py

### 🚀 Advanced Script

The advanced script improves on the foundational version by:

- Accepting an **optional directory path** as a parameter
- Defaulting to current working directory if none is passed
- **Recursively scanning** all subdirectories
- Returning each file’s:
  - `'name'`: file name
  - `'path'`: full file path
  - `'size'`: file size in bytes

**Key Script Enhancements:**
- Uses `os.walk()` for recursive traversal
- Adds path flexibility and deep directory coverage
- Better suited for audits, backups, and more complex use cases

---

### 🔍 Comparison Table

| Feature              | Foundational                | Advanced                            |
|----------------------|-----------------------------|--------------------------------------|
| Parameter Support    | ❌ None                     | ✅ Optional `path` parameter         |
| Recursion            | ❌ No                      | ✅ Yes (via `os.walk()`)            |
| Path Output          | ❌ Filename only           | ✅ Full path included               |
| File Filtering       | ✅ `os.path.isfile()`       | ✅ Recursive file validation        |
| Flexibility          | ❌ Fixed to `cwd`           | ✅ Custom paths supported           |

---

### 💡 Usage

```bash
# Run the foundational script
python list_files.py

# Run the advanced script (current directory)
python list_files_advanced.py

# Run the advanced script on a specific path
python list_files_advanced.py "C:/Users/Lamont/Documents"
```
Boto3 Section

## 📦 S3 Bucket Listing Script

This Python script (`list_buckets.py`) uses the boto3 library to authenticate with AWS and list all S3 buckets associated with the configured credentials.

### 🔧 What It Does
- Uses `boto3.client('s3')` to connect to AWS S3
- Calls `list_buckets()` to fetch all accessible buckets
- Prints each bucket name to the terminal

### ✅ Prerequisites
- AWS CLI installed and `aws configure` run with valid credentials
- boto3 installed (`pip install boto3`)
- Python 3.13 interpreter selected in VS Code

### 🚀 Run it
```bash
python list_buckets.py

---

### 📌 Author
Derrick Pope – Cloud Security Specialist & DevOps Enthusiast 🛡️⚙️  
GitHub: [pettymurphy](https://github.com/pettymurphy)
