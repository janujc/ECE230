import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csvFile = 'staticCharacteristicsInverter.csv'

data = pd.read_csv(csvFile)
inputVoltage = data.INPUT
outputVoltage = data.OUTPUT
revOutputVoltage = outputVoltage.reindex(index=outputVoltage.index[::-1])

length = len(outputVoltage)

maxAx = 4.5

x = np.arange(0,maxAx,maxAx/length)
y = np.arange(0,maxAx,maxAx/length)

def slope(index):
    if index < 5:
        return 0
    elif index >= (len(outputVoltage) - 5):
        return 0
    else:
        return (outputVoltage[index + 5] - outputVoltage[index - 5]) / (inputVoltage[index + 5] - inputVoltage[index - 5])

VDD = 5
VOH = max(outputVoltage) # max output voltage
VOL = min(outputVoltage) # min output voltage
VIH = next(inputVoltage[x[0]] for x in reversed(list(enumerate(outputVoltage))) if slope(x[0]) < -2)
VIL = next(inputVoltage[x[0]] for x in enumerate(outputVoltage) if slope(x[0]) < -1)

VOHA = np.full((length), VOH)
VOLA = np.full((length), VOL)
VIHA = np.full((length), VIH)
VILA = np.full((length), VIL)

plt.figure(1)
plt.axis([-0.1,maxAx,-0.1,maxAx])
plt.yticks([VOL,VOH], ('$V_{OL}$', '$V_{OH}$'))
plt.xticks([VOL,VIL,VIH,VOH], ('$V_{OL}$', '$V_{IL}$', '$V_{IH}$', '$V_{OH}$'))
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.plot(x, VOLA, 'k--', x, VOHA, 'k--', VILA, y, 'k--', VIHA, y, 'k--')
plt.plot(inputVoltage, outputVoltage)
plt.savefig("staticCharacteristicsInverter.png")
plt.show()