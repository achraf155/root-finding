from matplotlib import pyplot as plt
from time import time

def newtonRaphson(x0, es ):
    xr = x0 
    ea = 1
    x  = []; e =[] ; it = [] ## keep track of iterations, approximations, and roots
    i = 0 ## iteration counter
    while(es < ea): ## keep looping if the estimated value less than the approximated
        i+=1
        xrold = xr
        xr  = xrold - f(xrold) / df(xrold) ## the main formula based on the sloop of xi (beginning with x0 in our case) -> f'(xi) = f(xi) / (xi - xi+1)
        if(xr != 0):
            ea = abs((xr - xrold)/ xr) * 100 ##  approximation of error
        
        x.append(xr); e.append(ea); it.append(i)

    return x, e,it

##defined functions
def f(x) : return x ** 2 + x -5 ## function to solve 'it may be changed, but avoid functions that diverge'
def df(x) : return 2 * x + 1 ## primitive of f(x)

## main programm
start = time()
x , e, i = newton(1, 1E-8)
end = time()
print('newton raphson estimated time' , (end - start) * 100) ## print out the ammount time taken to find the root


## ploting the results using matplotlib module
plt.plot(i, e, color = 'y', label = 'Newton raphson')
plt.axis((1, 20, 1e-8, 1e2))
plt.yscale('log')
plt.xlabel('Itterations') ## number of Iterations in order to find the root as x values
plt.ylabel('Error') ## error approximations  as y values , as long as they get near to the eastimated error
plt.legend()
plt.show()

