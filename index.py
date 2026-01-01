#this is the file that should make the game work
import numpy as np
import sympy as sp
from pygnuplot import gnuplot as gp
import math as m

#TODO:
#woooooooooooooooooo ok im a litttle ahead of myself
#
#   simulate a population can simulate the following traits
#       1) individual members that have abatraraly many political opinions.
#            #these need to be able to be distinct or non distinct. (all people who like cats
#            #also like dogs, or vice verca)
#       2) above, with apathy
#       3) ability to produce political figures with specific ideas
#       4) size
#       5)
#math shit; its kinda beyond me what this does
x = sp.symbols('x')

## gnuplot setup
h = 60
w = h/2
# size '+ str(h)+','+str(m.floor(h/2))
plane = gp.Gnuplot(terminal = 'pngcairo',
    output = '"graph.png"',
    xrange= '[-10:10]'#,
    #yrange = '[ -2 to 2 ]'
)

plane.cmd('set samples 1000')



#define nomral function
plane.cmd('normal(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp(-0.5*((x-mu)/sigma)**2)')
def normal(x, mu=0, sigma=1):
    return 1/(sigma*m.sqrt(2*m.pi))* sp.exp(-0.5*((x-mu)/sigma)**2)
    #return f'1./({sigma}*sqrt(2*pi)) * exp(-0.5*((x-{mu})/{sigma})**2)'

#sp.diff(normal(x,0,1), x)



f1 = normal(x)
f2 = normal(x,5,3)

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

dogaxis = axis("dogs", [[f1,0.9], [f2,0.1]])
dogaxis.define()
#_______________________________________________________________________________
#1) Ceate a gnuplotuplot context. Set plotting style at initialization


#2) Set plotting style whenever needed.

#3) Expressions and caculations
plane.cmd(f'f1(x) = {f1}')
plane.cmd(f'f2(x) = {f2}')
#4) Plotting
#g.plot('d1(x) title "μ =  0.5 σ = 0.5"',
#        'd2(x) title "μ =  2.0 σ = 1.0"',
#        'd3(x) title "μ = -1.0 σ = 2.0
plane.plot('dogs(x) title "averaged function"'#,'f1(x)','f2(x)'
)
