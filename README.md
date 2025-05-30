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

---

## 💻 How to Run

Make sure you have Python 3 installed.

```bash
python list_files.py
