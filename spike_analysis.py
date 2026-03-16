import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = 100
time = np.arange(0, T, dt)

tau = 20
V_rest = -65
V_threshold = -50
V_reset = -65

V = np.zeros(len(time))
V[0] = V_rest

input_current = 1.5

for i in range(1, len(time)):
    dV = (-(V[i-1] - V_rest) + input_current) / tau
    V[i] = V[i-1] + dt * dV

    if V[i] >= V_threshold:
        V[i] = V_reset

plt.plot(time, V)
plt.title("Leaky Integrate-and-Fire Neuron")
plt.xlabel("Time")
plt.ylabel("Membrane Voltage (mV)")
plt.show()
