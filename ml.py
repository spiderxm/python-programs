#to print graph of tan 
import matplotlib.pyplot as plt 
import numpy as np
x=np.linspace(-10,10,100)
y=np.tan(x)
plt.plot(x,y,marker='x')
