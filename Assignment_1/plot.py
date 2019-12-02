import os
import matplotlib.pyplot as plt
import scipy, numpy, math 

i = [1,10,50,100]

fact_list = []
cube_list = []
exp_list = []
squared_list = []
log_list = []
root_list = []

for x in i:
    fact_list.append(scipy.math.factorial(x))
    cube_list.append(x**3)
    exp_list.append(2**x)
    squared_list.append(x*x)
    root_list.append(scipy.math.sqrt(x))
    log_list.append(math.log(x))


print ("fact",fact_list)
print ("cube",cube_list)
print ("exp", exp_list)
print ("squared",squared_list)
print ("log",log_list)
print ("linear", i)
print ("root", root_list)

plt.xlim(0,100)
plt.ylim(0, 100)
plt.plot(i, fact_list, "r", label="Factorial")
plt.plot(i, cube_list, "b", label="Cubic")
plt.plot(i, exp_list, "g", label="Exponential")
plt.plot(i, i, "black", label="Linear")
plt.plot(i, root_list, "black", label="Root")

plt.plot(i, squared_list, "y", label="Squared")
plt.plot(i, log_list, "#6bb1bf", label="Logarithmic")
plt.legend()
plt.show()