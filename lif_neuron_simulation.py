import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation Parameters
# -----------------------------
# dt = time step (ms)
# T = total simulation time (ms)

dt = 0.1
T = 100
time = np.arange(0, T, dt)

# -----------------------------
# Neuron Model Parameters
# -----------------------------
# tau = membrane time constant
# V_rest = resting membrane potential (mV)
# V_threshold = spike threshold (mV)
# V_reset = voltage after a spike occurs

tau = 20
V_rest = -65
V_threshold = -50
V_reset = -65

# -----------------------------
# Initialize membrane voltage
# -----------------------------
# Create an array to store voltage over time
# Start neuron at resting potential

V = np.zeros(len(time))
V[0] = V_rest

# Constant input current driving the neuron
input_current = 1.5

# -----------------------------
# Simulate neuron dynamics
# -----------------------------
# Using the leaky integrate-and-fire model

for i in range(1, len(time)):

    # Differential equation for membrane voltage
    dV = (-(V[i-1] - V_rest) + input_current) / tau

    # Euler integration step
    V[i] = V[i-1] + dt * dV

    # Check if neuron fires a spike
    if V[i] >= V_threshold:
        V[i] = V_reset

# -----------------------------
# Plot results
# -----------------------------

plt.plot(time, V)
plt.title("Leaky Integrate-and-Fire Neuron Simulation")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Voltage (mV)")
plt.show()
