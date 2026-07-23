import matplotlib.pyplot as plt
import numpy as np

students = ["Ali", "Sara", "Ahmed", "Ayesha", "Zain", "Hamza"]
marks = [78, 92, 85, 96, 74, 88]

plt.plot(
    students,
    marks,
    marker='o',
    linestyle='--',
    linewidth=2,
    color='red'
)
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("marks")
plt.grid(True)
plt.show()