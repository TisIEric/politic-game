#this is the file that should make the game work
import numpy as np
from pygnuplot import gnuplot
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
#1) Ceate a gnuplot context. Set plotting style at initialization
g = gnuplot.Gnuplot(terminal = 'pngcairo transparent enhanced ' +
        'font "nimbus,8" fontscale 1.0 size 512, 280 ',
        output = '"quick_example.png"',
        style = ["fill transparent solid 0.50 noborder",
            "data lines",
            "function filledcurves y1=0"],
        key = 'title "Gaussian Distribution" center fixed left top vertical '+
        'Left reverse enhanced autotitle nobox noinvert samplen 1 ' +
        'spacing 1 width 0 height 0',
        title = '"Transparent filled curves"',
        xrange = '[ -5.00000 : 5.00000 ] noreverse nowriteback',
        yrange = '[ 0.00000 : 1.00000 ] noreverse nowriteback')

#2) Set plotting style whenever needed.

#3) Expressions and caculations
g.cmd('Gauss(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp( -(x-mu)**2 / (2*sigma**2) )',
        'd1(x) = Gauss(x, 0.5, 0.5)',
        'd2(x) = Gauss(x,  2.,  1.)',
        'd3(x) = Gauss(x, -1.,  2.)')

#4) Plotting
g.plot('d1(x) fs solid 1.0 lc rgb "forest-green" title "μ =  0.5 σ = 0.5"',
        'd2(x) lc rgb "gold" title "μ =  2.0 σ = 1.0"',
        'd3(x) lc rgb "dark-violet" title "μ = -1.0 σ = 2.0"')
