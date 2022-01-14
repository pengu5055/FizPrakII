import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#with open("delta.csv", "r", encoding="utf-8") as f:
#    deltas = [i[:-1] for i in f.readlines()]
#    f.close()
#
#plt.hist(deltas, bins=25)
#plt.xlabel("$\Delta t [s]$")
#plt.ylabel("St. Meritev")
#plt.title("Stevilo casovnih intervalov med zaporednima sunkoma v odvisnosti od dolzine intervalov")
#plt.show()
c = np.loadtxt("UrbancMarko_absorpcija_3.txt", usecols=1, skiprows=2)
deltas = np.empty(c.size)
deltas[0] = c[0]
for i in range(1, c.size):
    deltas[i] = c[i]-c[i-1]
print(deltas)
#hist = np.histogram(deltas, bins=[0, 1])
plt.hist(deltas, bins="auto", color="teal")
plt.title("St. casovnih int. med zap. sunkoma v odvisnosti od dolzine int.")
plt.xlabel(r"$\Delta t[s]$")
plt.ylabel("Stevilo meritev")
plt.axvline(x=np.mean(deltas), ls="dotted", color="orange")
plt.text(0.18, 100, r"$\overline{\Delta t}$ = "+str(round(np.mean(deltas), 5))+" s", fontsize=14)
plt.savefig("histogram.png", format="png")
plt.clf()