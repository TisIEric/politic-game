#see that fancy formatting there??? pretty cool huh
#thanks to @statswithbrian on youtube
#from numpy.random import random
import numpy                    as np
from sympy     import *
from PyGnuplot import gp
from sympy.abc import i
import math                     as m


x = symbols('x')
y = symbols('y')
## gnuplot setup
h = 60#unused
solveResolution=10**-3#this is the number that the function is subtracted by
w = 10

samples = 5000
pngTerminal = True
if pngTerminal:
    GPterminal = "pngcairo"
    GPoutput = "graph.png"
else:
    GPterminal = f'dumb size {h*3}, {h}'
    GPoutput = "graph.txt"
plane = gp()
plane.terminal =f'{GPterminal} '
plane.output = f'"{GPoutput}"'
plane.xrange= f'[-{w}:{w}+5]'
plane.yrange = '[ 0 to 1 ]'


plane.c(f'set samples {samples}')

def normal(mu=0, sigma=1,x=x):
    return 1/(sigma*m.sqrt(2*m.pi))* exp(-0.5*((x - mu)/sigma)**2)

functionIterator = 1


class normalContainer:
    def __init__(self, indicator="f"):
        self.normals = {}
        self.indicator = indicator
        self.i = 1

    def addNormal(self, mu=0, sigma=1,cause="noName"):

        if cause=="noName" or cause ==f"{self.indicator}{self.i}":
            cause = f"{self.indicator}{self.i}"
            self.i += 1

        self.normals[cause] = normal(mu, sigma,x)
        plane.c(f'{cause}(x) = {self.normals[cause]}')

class axis:
    def __init__(self, subject, factors):
        #factors have a function and a weight in a list [function, weight]
        self.rule = averageNormals(factors)
        self.densityRule = self.rule
        #|^this is just to make some things more readable
        self.cumulativeRule = integrate(self.rule,(x,-oo,x))

        self.subject = subject
        self.factors = factors
    def define(self):
        self.rule = averageNormals(self.factors)
        self.densityRule = self.rule
        self.cumulativeRule = integrate(self.rule,(x,-oo,x))
        plane.c(f'{self.subject}(x) = {self.rule}')
    def setRule(self):
        self.rule = averageNormals(self.factors)
    def addFactor(self, function, weight):
        for curve in self.factors:
            curve[1] -= weight/len(self.factors)
        self.factors.append([function, weight])

        self.define()



def averageNormals(inputs):
    #input should be a list of  functions
    output = 0
    weightTotal = 0
    for factor in inputs:
        #NOTE the weights are off because of floating point impresicion.
        #|I am just too lazy to fix it
        output += factor[0]*factor[1]
        weightTotal += factor[1]
    if weightTotal > 1:
        print("\nFUNCTION AVERAGE ERROR: sum of weights too LARGE\n")
    elif weightTotal < 1:
        print("\nFUNCTION AVERAGE ERROR: sum of weights too SMALL")

    return output
def jointNormalsProbilty(inputs, lower_limit=-oo, upper_limit=x):
    #HERE inputs IS ASKING FOR A LIST OF JUST THE FUNCTIONS!!!!
    #very important folks, not a lot of people know this.
    output = 1
    for function in inputs:
        output = output * integrate(function, (x, lower_limit, upper_limit))
    return diff(ouput)


glob = normalContainer()
glob.addNormal(cause="COcats")
glob.addNormal(cause="COdogs")
glob.addNormal(-2,0.3)
glob.addNormal(cause="test")

#f4 = normal
#define axes
dogaxis = axis("dogs", [[glob.normals["COdogs"],1]])
dogaxis.define()

cataxis = axis("cats", [[glob.normals["COcats"],1.0]])

cataxis.addFactor(glob.normals["f1"],0.9)
cataxis.define()

f_inv = solve(dogaxis.cumulativeRule-i, x)[0]
i = 0
while i < 100:
    ex = np.random.uniform(0, 1)
    wygh = f_inv
    wygh = f_inv.subs(x, wygh).evalf()
    plane.c(f'set object circle at first {ex},dogs({ex}) radius char 0.5')
    i += 1


    #on a scale from -1 to 1
    # posibly the merger of multiple gausian functions.

plane.c(f'doginv(x) = {dogaxis.cumulativeRule}')

#plane.c(f'a(x) = {dogaxis.cumulativeRule}')
#this is debug thing really
#plane.plot('dogs(x)','doginv(x)'#,f'{f_inv}')
plane.save('dogs(x)','doginv(x)',"tmp.dat")
plane.a('plot "tmp.dat"')
print(f_inv)
