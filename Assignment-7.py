import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = {"Student": ["Amit", "Esha", "Farhan", "Maya", "Sudeep"],
"Maths": [78, 86, 91, 69, 88],
"Python": [87, 95, 75, 84, 73],
"Attendance": [89, 93, 74, 98, 82],
"City": ["Pune", "Mumbai", "Nashik", "Pune", "Mumbai"]}

df = pd.DataFrame(data)

print(df.head())

# 2. Line Graph
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 3. Bar Graph
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 5. Correlation Matrix & Heatmap
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
