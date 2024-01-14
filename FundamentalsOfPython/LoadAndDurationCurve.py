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


# Example data for load and duration curves
load_data = {
    "time": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "load": [1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 0]
}

# Sort data for duration curve
sorted_load_data = sorted(
    load_data.items(), key=lambda item: item[1], reverse=True)
duration_time = [i[0] for i in sorted_load_data]
duration_load = [i[1] for i in sorted_load_data]

# Plot load curve
plt.figure(figsize=(10, 6))
plt.plot(load_data["time"], load_data["load"], marker='o', label='Load (MW)')
plt.xlabel('Time (Hours)')
plt.ylabel('Load (MW)')
plt.title('Load Curve')
plt.grid(True)
plt.legend()

# Plot duration curve
plt.figure(figsize=(10, 6))
plt.plot(duration_time, duration_load, marker='o', label='Load (MW)')
plt.xlabel('Time Exceeded (Hours)')
plt.ylabel('Load (MW)')
plt.title('Duration Curve')
plt.grid(True)
plt.legend()

# Show the plots
plt.show()
