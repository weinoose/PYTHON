import matplotlib.pyplot as plt
import numpy as np

# BASIC GRAPH

# Defininig the X, Y Values.
x = [1,2,3,4,5]
y = [1,4,9,16,25]

# Adding X,Y values to the plot.
plt.plot(x,y)
# Defining the X,Y points on plot.
plt.axis([1,5,1,25])

# Final Part.
plt.title("BASIC PLOT")
plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")
plt.show()

# MULTI GRAPH

x = np.linspace(1,5,5)
plt.plot(x, x, label = "linear", color="green")
plt.plot(x, x**2, label = "quadratic", color="yellow")
plt.plot(x, x**3, label = "cubic", color="red")

plt.xlabel("X VALUES")
plt.ylabel("Y VALUES")

plt.title("MULTIPLE PLOT")
plt.legend()

plt.show()

# SPLITTED PLOT

x = np.linspace(1,10,10)
fig,axs =  plt.subplots(3)

axs[0].plot(x, x, color="red")
axs[0].set_title("Linear")

axs[1].plot(x, x**2, color="green")
axs[1].set_title("Quadratic")

axs[2].plot(x, x**3, color="yellow")
axs[2].set_title("Cubic")

plt.tight_layout()

plt.show() 

# SPLITTED PLOT VOL. 2

x = np.linspace(0,10,11)
fig,axs =  plt.subplots(2,2)
fig.suptitle("SPLITTED PLOT")

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")

plt.show() 

# MATHEMATICAL GRAPH

x = np.linspace(-25,24,25)
y = x ** 3
z = x ** 2

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(10,10))

axes[0].plot(x,y)
axes[0].set_title("f(x)=x^3")
axes[1].plot(x,z)
axes[1].set_title("f(x)=x^2")
plt.tight_layout()

plt.show()