import matplotlib.pyplot as plt

# Define load data
load_data = {
    "00:00-04:00": 1500,
    "04:00-08:00": 2800,
    "08:00-12:00": 4500,
    "12:00-16:00": 5000,
    "16:00-20:00": 4200,
    "20:00-00:00": 3000,
}

# Extract time and load values
time_labels = list(load_data.keys())
load_values = list(load_data.values())

# Create load curve
plt.figure(figsize=(10, 6))
plt.plot(time_labels, load_values, marker='o', label='Load (MW)')
plt.xlabel('Time Period')
plt.ylabel('Load (MW)')
plt.title('Load Curve')
plt.grid(True)

# Calculate cumulative load duration
cumulative_duration = 0
duration_data = []
for load in load_values:
    cumulative_duration += 4  # Assuming 4 hours per time period
    duration_data.append(cumulative_duration)

# Create duration curve
plt.figure(figsize=(10, 6))
plt.plot(load_values, duration_data, marker='o', label='Duration (hours)')
plt.xlabel('Load (MW)')
plt.ylabel('Cumulative Duration (hours)')
plt.title('Duration Curve')
plt.grid(True)

# Show both curves
plt.show()
