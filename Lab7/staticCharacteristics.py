import numpy as np
import matplotlib.pyplot as plt

length = 250
maxAx = 4.5

x = np.arange(0,maxAx,maxAx/length)
y = np.arange(0,maxAx,maxAx/length)

vol=0.5
voh=5.0
vil=1.5
vih=4.0

# curve equation = f(x) = L - L/(1 + exp[-k(x - xn)])

def logistic(L, k, x, mid):
	return L - (L - vol)/(1 + np.exp(-(k) * (x - mid)))

c = []

for i in x:
	c.append(logistic(voh, 4, i, (voh + vol) / 2))

voha = np.full((length), voh)
vola = np.full((length), vol)
viha = np.full((length), vih)
vila = np.full((length), vil)

plt.figure(1)
plt.axis([0,maxAx,0,maxAx])
plt.yticks([vol,voh], ('$V_{OL}$', '$V_{OH}$'))
plt.xticks([vol,vil,vih,voh], ('$V_{OL}$', '$V_{IL}$', '$V_{IH}$', '$V_{OH}$'))
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.plot(x, vola, 'k--', x, voha, 'k--', vila, y, 'k--', viha, y, 'k--')
plt.plot(x, c, 'k-')
plt.savefig("staticCharInv.png")
plt.show()