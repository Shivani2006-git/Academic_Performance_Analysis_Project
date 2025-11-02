# ===============================
# 📘 Academic Performance Distribution in Schools
# ===============================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os

# Step 2: Extract Dataset from ZIP File
zip_path = r"C:\Users\LENOVO\Downloads\archive.zip"
extract_dir = r"C:\Users\LENOVO\Downloads\student_data"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
    print("Dataset extracted successfully!")
    print("Files extracted:")
    print(zip_ref.namelist())

# Step 3: Load Dataset
csv_path = os.path.join(extract_dir, 'StudentsPerformance.csv')
data = pd.read_csv(csv_path)
print("\n🔹 Dataset Loaded Successfully!")
print("Shape of data:", data.shape)
print("\nFirst 5 rows:")
print(data.head())

# Step 4: Check Data Info, Missing Values, and Summary Stats
print("\n🔹 Dataset Info:")
print(data.info())

print("\n🔹 Missing values:")
print(data.isnull().sum())

print("\n🔹 Summary Statistics:")
print(data.describe())

# Step 5: Clean Column Names (remove spaces)
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 6: Create an Average Score Column
data['average_score'] = data[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Step 7: Visualization Setup
sns.set(style="whitegrid", palette="pastel", font_scale=1.1)

# 7A. Gender vs Average Score
plt.figure(figsize=(7, 5))
sns.barplot(x='gender', y='average_score', data=data, hue='gender', palette='Set2', legend=False)
plt.title("Average Performance by Gender", fontsize=14, fontweight='bold')
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()

# 7B. Parental Education vs Average Score
plt.figure(figsize=(10, 6))
sns.barplot(x='parental_level_of_education', y='average_score', data=data,
            hue='parental_level_of_education', palette='cool', legend=False)
plt.title("Impact of Parental Education on Student Performance", fontsize=14, fontweight='bold')
plt.xlabel("Parental Level of Education")
plt.ylabel("Average Score")
plt.xticks(rotation=30)
plt.show()

# 7C. Test Preparation Course vs Average Score
plt.figure(figsize=(6, 5))
sns.barplot(x='test_preparation_course', y='average_score', data=data,
            hue='test_preparation_course', palette='magma', legend=False)
plt.title("Effect of Test Preparation on Performance", fontsize=14, fontweight='bold')
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.show()

# 7D. Lunch Type vs Average Score
plt.figure(figsize=(6, 5))
sns.barplot(x='lunch', y='average_score', data=data,
            hue='lunch', palette='viridis', legend=False)
plt.title("Average Score by Lunch Type", fontsize=14, fontweight='bold')
plt.xlabel("Lunch Type")
plt.ylabel("Average Score")
plt.show()

# Step 8: Insights
print("\n🔹 Average overall performance by gender:")
print(data.groupby('gender')['average_score'].mean())

print("\n🔹 Average overall performance by parental education:")
print(data.groupby('parental_level_of_education')['average_score'].mean())

# Step 9: Save Cleaned Dataset
output_path = os.path.join(extract_dir, 'cleaned_student_performance.csv')
data.to_csv(output_path, index=False)
print(f"\n✅ Cleaned dataset saved at: {output_path}")
