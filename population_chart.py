import matplotlib.pyplot as plt

# Data
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]

# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(age_groups, population, color=['yellow', 'blue', 'magenta'])

# Adding labels
plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Group")
plt.ylabel("Population (in Millions)")
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'{yval} Mn', ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
