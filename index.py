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

## gnuplot setup
h = 60
w = h/2
# size '+ str(h)+','+str(m.floor(h/2))
plane = gp.Gnuplot(terminal = 'pngcairo',
    output = '"graph.png"'#,
    #xrange= '[-2.5:2.5]',
    #yrange = '[ -2 to 2 ]'
)

plane.cmd('set samples 1000')



#define nomral function
plane.cmd('normal(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp(-0.5*((x-mu)/sigma)**2)')
def normal(mu,sigma):
    return 1/sigma*m.sqrt(2*m.pi)
    #return f'1./({sigma}*sqrt(2*pi)) * exp(-0.5*((x-{mu})/{sigma})**2)'

def writeRule():
    pass

class axis:
    def __init__(self, subject, mu=0, sigma=1):
        self.rule = normal(mu,sigma)
        self.subject = subject
    def declare(self):
        plane.cmd(f'{self.subject}(x) = '+self.rule)
    #on a scale from -1 to 1
    # posibly the merger of multiple gausian functions.
dogaxis = axis("dogs")
dogaxis.declare()
#_______________________________________________________________________________
#1) Ceate a gnuplotuplot context. Set plotting style at initialization


#2) Set plotting style whenever needed.

#3) Expressions and caculations
#plane.cmd('')

#4) Plotting
#g.plot('d1(x) title "μ =  0.5 σ = 0.5"',
#        'd2(x) title "μ =  2.0 σ = 1.0"',
#        'd3(x) title "μ = -1.0 σ = 2.0"')
plane.plot('dogs(x) title "opinioin of dogs"')
