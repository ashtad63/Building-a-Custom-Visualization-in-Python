#%%
import numpy as np
import matplotlib.pyplot as plt

m = np.zeros((1,21))
for i in range(21):
    m[0,i] = (i*5)/100.0
print (m)
plt.imshow(m, cmap='seismic', aspect=2)
plt.yticks(np.arange(0))
plt.xticks(np.arange(0,25,5), [0,25,50,75,100])
plt.show()