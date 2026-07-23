import matplotlib.pyplot as plt

study_hours = [1,2,3,4,5,6,7,8,9,10]

marks = [42,50,58,63,69,74,81,87,92,97]



plt.scatter(
    study_hours,
    marks,
    color="crimson",
    s=120
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()