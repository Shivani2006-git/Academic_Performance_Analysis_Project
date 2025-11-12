# ===============================
# 📘 Academic Performance Distribution in Schools
# ===============================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset directly from GitHub
url = "https://raw.githubusercontent.com/Shivani2006-git/Academic_Performance_Analysis_Project/main/student_data/StudentsPerformance.csv"

try:
    data = pd.read_csv(url)
    print("✅ Dataset loaded successfully from GitHub!")
except Exception as e:
    print("❌ Error loading dataset. Please check the GitHub link.")
    print(e)

# Step 3: Data Info
print("Shape of data:", data.shape)
print("\nFirst 5 rows:")
print(data.head())

# Step 4: Clean Column Names
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 5: Create an Average Score Column
data['average_score'] = data[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Step 6: Visualization Setup
sns.set(style="whitegrid", palette="pastel", font_scale=1.1)

# Gender vs Average Score
plt.figure(figsize=(7, 5))
sns.barplot(x='gender', y='average_score', data=data, hue='gender', palette='Set2', legend=False)
plt.title("Average Performance by Gender", fontsize=14, fontweight='bold')
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()

# Parental Education vs Average Score
plt.figure(figsize=(10, 6))
sns.barplot(x='parental_level_of_education', y='average_score', data=data,
            hue='parental_level_of_education', palette='cool', legend=False)
plt.title("Impact of Parental Education on Student Performance", fontsize=14, fontweight='bold')
plt.xlabel("Parental Level of Education")
plt.ylabel("Average Score")
plt.xticks(rotation=30)
plt.show()

# Test Preparation Course vs Average Score
plt.figure(figsize=(6, 5))
sns.barplot(x='test_preparation_course', y='average_score', data=data,
            hue='test_preparation_course', palette='magma', legend=False)
plt.title("Effect of Test Preparation on Performance", fontsize=14, fontweight='bold')
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.show()

# Lunch Type vs Average Score
plt.figure(figsize=(6, 5))
sns.barplot(x='lunch', y='average_score', data=data,
            hue='lunch', palette='viridis', legend=False)
plt.title("Average Score by Lunch Type", fontsize=14, fontweight='bold')
plt.xlabel("Lunch Type")
plt.ylabel("Average Score")
plt.show()

# Step 7: Insights
print("\n🔹 Average overall performance by gender:")
print(data.groupby('gender')['average_score'].mean())

print("\n🔹 Average overall performance by parental education:")
print(data.groupby('parental_level_of_education')['average_score'].mean())
