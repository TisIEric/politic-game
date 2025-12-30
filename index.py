#this is the file that should make the game work
import numpy as np
from pygnuplot import gnuplot as gp
import math as m

#TODO:
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
plane = gp.Gnuplot(terminal = 'dumb size '+ str(h)+','+str(m.floor(h/2)),
    output = '"graph.txt"',
    xrange= '[-2.5:2.5]',
    yrange = '[ -2 to 2 ]')

plane.cmd('set samples 1000')



#define nomral function
plane.cmd('normal(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp( -(x-mu)**2 / (2*sigma**2) )')
def normal(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)

    return prob_density

mean = 0
sd = 1
x = 1
result = normal(x, mean, sd)
print(result)




class opinion:
    pass
    #on a scale from -1 to 1
    # posibly the merger of multiple gausian functions.
#_______________________________________________________________________________
#1) Ceate a gnuplotuplot context. Set plotting style at initialization


#2) Set plotting style whenever needed.

#3) Expressions and caculations
plane.cmd(
    'b(x) = exp(-x**2)',
    'f1(x) = b(x)',
    'f2(x) = -b(x)',
    'f3(x) = sin(x)*b(x)',
        'd1(x) = Gauss(x, 0.5, 0.5)',
        'd2(x) = Gauss(x,  2.,  1.)',
        'd3(x) = Gauss(x, -1.,  2.)')

#4) Plotting
#g.plot('d1(x) title "μ =  0.5 σ = 0.5"',
#        'd2(x) title "μ =  2.0 σ = 1.0"',
#        'd3(x) title "μ = -1.0 σ = 2.0"')
plane.plot('f1(x)','f2(x)','f3(x)')
