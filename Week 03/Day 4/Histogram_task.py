import matplotlib.pyplot as plt

ages = [
18,19,20,21,20,19,22,18,20,21,
19,20,22,23,20,21,22,19,20,18,
20,21,22,23,19,20,21,18,22,20
]

plt.figure(figsize=(8,5))

plt.hist(
    ages,
    bins=6,
    color="skyblue",
    edgecolor="black"
)

plt.title("Student Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")

plt.show()

