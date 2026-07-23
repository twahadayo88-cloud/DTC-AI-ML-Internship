import numpy as np
marks = np.array([
    [80, 75, 90],
    [70, 85, 95],
    [60, 65, 70]
])

print("marks")
print(marks)

print("\nAverage Marks")
print(np.mean(marks))

print("\nStandard Deviation")
print(np.std(marks))

print("\nHighest Marks")
print(np.max(marks))

print("\nLowest Marks")
print(np.min(marks))

normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))

print("\nNormalized Marks")
print(normalized)