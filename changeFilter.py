import numpy as np
import matplotlib.pyplot as plt

def expofilter(f,alpha,x):
    return alpha*f+(1-alpha)*x

def changeDetect(data,alpha,threshold):
    fvalues = data[0]*np.ones(len(data))
    changevalues = np.zeros(len(data))
    changepos = []
    for i in range(1,len(data)):
        fvalues[i] = expofilter(fvalues[i-1],alpha,data[i])
        changevalues[i] = abs(fvalues[i]-fvalues[i-1])
        if changevalues[i]>threshold:
            changepos = np.append(changepos,i)
    return changevalues,changepos
            
data = np.random.randint(-4,4,100)
data[50] += 20
data[51] += 20
data[52] += 20
fullfilter,changepositions = changeDetect(data,0.9,1.5)
plt.plot(fullfilter)
plt.title('Figure to show the Full Filter Response')
plt.xlabel('Index')
plt.ylabel('Change Signal Value')
plt.show()
