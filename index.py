#this is the file that should make the game work
import numpy as np
import sympy as sp
from pygnuplot import gnuplot as gp
import math as m

#math shit; its kinda beyond me what this does. gonna look up what symbols
#are at some point
x = sp.symbols('x')

## gnuplot setup
h = 60
w = 10
# size '+ str(h)+','+str(m.floor(h/2))
plane = gp.Gnuplot(terminal = 'pngcairo',
    output = '"graph.png"',
    xrange= f'[-{w}:{w}]',
    yrange = '[ 0 to  ]'
)

plane.cmd('set samples 1000')


#>>MAYBE DELETE<<
#define nomral function.
#plane.cmd('normal(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp(-0.5*((x-mu)/sigma)**2)')

def normal(x, mu=0, sigma=1):
    return 1/(sigma*m.sqrt(2*m.pi))* sp.exp(-0.5*((x-mu)/sigma)**2)
    #return f'1./({sigma}*sqrt(2*pi)) * exp(-0.5*((x-{mu})/{sigma})**2)'


f1 = normal(x)
plane.cmd(f'f1(x) = {f1}')

f2 = normal(x,5,3)
plane.cmd(f'f2(x) = {f2}')


def averagedNormal(inputs):
    #input should be a list of  functions
    output = 0
    weightTotal = 0
    for factor in inputs:
        output += factor[0]*factor[1]
        weightTotal += factor[1]
    print(weightTotal)
    if weightTotal > 1:
        print("\nFUNCTION AVERAGE ERROR: sum of weights too LARGE\n")
    elif weightTotal < 1:
        print("\nFUNCTION AVERAGE ERROR: sum of weights too SMALL")

    return output



class axis:
    def __init__(self, subject, factors):
        #factors have a function and a weight in a list [function, weight]
        self.rule = averagedNormal(factors)
        self.subject = subject
        self.factors = factors
    def define(self):
        plane.cmd(f'{self.subject}(x) = {self.rule}')
    def setRule(self):
        self.rule = averagedNormal(self.factors)
    def addFactor(self, function, weight):
        self.factors += []

    #on a scale from -1 to 1
    # posibly the merger of multiple gausian functions.

#define axes
dogaxis = axis("dogs", [[f1,0.9], [f2,0.1]])
dogaxis.define()

#this is debug thing really
plane.plot('dogs(x) title "averaged function"'#,'f1(x)','f2(x)'
)
