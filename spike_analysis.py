import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load spike time data
# -----------------------------
# Example spike times (seconds)
# Later you can replace this with real spike data

spike_times = np.array([
0.1, 0.15, 0.23, 0.31, 0.47, 0.52,
0.60, 0.72, 0.85, 0.91, 1.03, 1.15
])

# -----------------------------
# Compute firing rate
# -----------------------------
duration = spike_times[-1] - spike_times[0]
firing_rate = len(spike_times) / duration

print("Total spikes:", len(spike_times))
print("Recording duration:", duration, "seconds")
print("Firing rate:", firing_rate, "Hz")

# -----------------------------
# Compute interspike intervals
# -----------------------------
isi = np.diff(spike_times)

# -----------------------------
# Plot spike raster
# -----------------------------
plt.figure()

plt.eventplot(spike_times)
plt.title("Spike Raster Plot")
plt.xlabel("Time (s)")
plt.yticks([])

plt.savefig("spike_raster.png")
plt.show()

# -----------------------------
# Plot ISI histogram
# -----------------------------
plt.figure()

plt.hist(isi, bins=10)
plt.title("Interspike Interval Distribution")
plt.xlabel("Interval (s)")
plt.ylabel("Count")

plt.show()
