import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Load dataset ----------------

data = pd.read_excel("students.xlsx")

print("First 5 rows of data:")
print(data.head())

print("\nDataset Information:")
data.info()

print("\nStatistical Summary:")
print(data.describe())

print("\nColumn Names:")
print(data.columns)


# ---------------- BI Visualizations ----------------

# 1 Bar Chart
plt.figure()
plt.bar(data["NAME"], data["MARKS"])
plt.title("Student Marks Comparison")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()


# 2 Pie Chart
plt.figure()
plt.pie(data["MARKS"], labels=data["NAME"], autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()


# 3 Histogram
plt.figure()
plt.hist(data["MARKS"], bins=5)
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()


# 4 Box Plot
plt.figure()
plt.boxplot(data["MARKS"])
plt.title("Marks Spread Analysis")
plt.ylabel("Marks")
plt.show()


# 5 Scatter Plot
plt.figure()
plt.scatter(data["AGE"], data["MARKS"])
plt.title("Age vs Marks Relationship")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()


# 6 Line Chart
plt.figure()
plt.plot(data["NAME"], data["MARKS"], marker="o")
plt.title("Marks Line Chart")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()


# 7 Horizontal Bar Chart
plt.figure()
plt.barh(data["NAME"], data["MARKS"])
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Student")
plt.show()


# 8 Marks Trend
plt.figure()
plt.plot(data["MARKS"])
plt.title("Marks Trend")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()


# 9 Age Pie Chart
plt.figure()
plt.pie(data["AGE"], labels=data["NAME"], autopct='%1.1f%%')
plt.title("Age Distribution")
plt.show()


# 10 Bigger Scatter
plt.figure()
plt.scatter(data["AGE"], data["MARKS"], s=100)
plt.title("Age vs Marks Analysis")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()


# ---------------- Business Insights ----------------

print("\nBusiness Insights")

print("Average Marks:", data["MARKS"].mean())
print("Highest Marks:", data["MARKS"].max())
print("Lowest Marks:", data["MARKS"].min())

print("Average Age:", data["AGE"].mean())
print("Max Age:", data["AGE"].max())
print("Min Age:", data["AGE"].min())

top = data.loc[data["MARKS"].idxmax()]
print("Top Student:", top["NAME"])