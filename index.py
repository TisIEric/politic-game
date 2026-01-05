#see that fancy formatting there??? pretty cool huh
#from numpy     import *
from sympy     import *
from pygnuplot import gnuplot as gp
import math                   as m


#math shit; its kinda beyond me what this does. gonna look up what symbols
#are at some point
x = symbols('x')

## gnuplot setup
h = 60#unused
w = 10

samples = 5000
pngTerminal = True
if pngTerminal:
    GPterminal = "pngcairo"
    GPoutput = "graph.png"
else:
    GPterminal = f'dumb size {h*3}, {h}'
    GPoutput = "graph.txt"
plane = gp.Gnuplot(terminal = f'{GPterminal} ',
    output = f'"{GPoutput}"',
    xrange= f'[-{w}:{w}+5]',
    yrange = '[ 0 to  ]'
)

plane.cmd(f'set samples {samples}')

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
        plane.cmd(f'{cause}(x) = {self.normals[cause]}')

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
        plane.cmd(f'{self.subject}(x) = {self.rule}')
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
glob.addNormal()

#f4 = normal
#define axes
dogaxis = axis("dogs", [[glob.normals["COdogs"],1]])
dogaxis.define()

cataxis = axis("cats", [[glob.normals["COcats"],1.0]])

cataxis.addFactor(glob.normals["f1"],0.9)
print(cataxis.factors[0][1])
cataxis.define()



    #on a scale from -1 to 1
    # posibly the merger of multiple gausian functions.



#plane.cmd(f'a(x) = {dogaxis.cumulativeRule}')
#this is debug thing really
plane.plot('dogs(x) title "the dog one"', 'cats(x) title "the cat one"'
)
