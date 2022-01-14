import numpy as np
import matplotlib.pyplot as plt

c = np.loadtxt("UrbancMarko_absorpcija_3.txt", usecols=1, skiprows=2)
deltas = np.empty(c.size)
deltas[0] = c[0]
for i in range(1, c.size):
    deltas[i] = c[i]-c[i-1]
print(deltas)
#hist = np.histogram(deltas, bins=[0, 1])
plt.hist(deltas, bins="auto")
plt.title("Število intervalov med dvema razpadoma v odvisnosti od dolžine intervala")
plt.xlabel(r"$\Delta t$ [s]")
plt.ylabel(r"$Št. meritev$ [1]")
plt.axvline(x=np.mean(deltas), ls="--", color="r")
plt.text(0.2, 130, r"$\overline{\Delta t}$ = "+str(round(np.mean(deltas),5))+" s", fontsize=14)
plt.savefig("histogram.png", format="png")
plt.clf()