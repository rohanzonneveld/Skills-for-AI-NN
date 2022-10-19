# plot
import matplotlib.pyplot as plt
import sys
plt.rcParams["figure.figsize"] = [15.0, 7.00]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.matshow(correlation, cmap='YlGn')

for i in range(12):
   for j in range(12):
      c = np.around(correlation[j][i],2)
      ax.text(i, j, str(c), va='center', ha='center')

plt.show()
sys.exit()