import os
import pandas as pd

# Base paths
base_dir = r"C:\Users\anany\Desktop\anemic detection"
excel_files = ["india_data.xlsx.xlsx", "italy_data.xlsx.xlsx"]  # ✅ exact names
images_base = os.path.join(base_dir, "images", "archive (1)", "dataset anemia")

# Loop over both Excel files
for excel_file in excel_files:
    file_path = os.path.join(base_dir, excel_file)  # look directly in main folder

    if not os.path.exists(file_path):
        print(f" File NOT found: {file_path}")
        continue

    # Read Excel
    try:
        df = pd.read_excel(file_path)
        print(f"\n Processing file: {excel_file}")
        print(df.head())
    except Exception as e:
        print(f" Error reading {excel_file}: {e}")
        continue

    # Detect country name from file
    if "india" in excel_file.lower():
        country = "India"
    else:
        country = "Italy"

    country_path = os.path.join(images_base, country)

    if not os.path.exists(country_path):
        print(f" Country folder not found: {country_path}")
        continue

    # Check each patient folder
    for patient_num in df["Number"]:
        patient_folder = os.path.join(country_path, str(patient_num))
        if os.path.exists(patient_folder):
            print(f" Found folder for patient {patient_num} in {country}")
        else:
            print(f" Patient folder NOT found for number {patient_num} in {country}")

print("\n Done checking all patients for India & Italy!")
