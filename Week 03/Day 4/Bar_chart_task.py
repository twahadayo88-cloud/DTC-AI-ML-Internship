import matplotlib.pyplot as plt
import numpy as np

departments = ["IT", "HR", "Finance", "Marketing", "Sales"]

employees = [28, 12, 18, 15, 25]


plt.bar(
    departments,
    employees,
    color=["blue","green","orange","purple","red"]
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()