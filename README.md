This is a "game" that uses combined normal distributions to make what appears to be a convincing simulation of a modern political landscape. Made by me, AEric. I have made great use of Desmos, Python, and Gnuplot on this project.
# mathamatical concepts
*p.s. most of this information comes from either wikipedia or me putting random numbers into Desmos*
A Gaussian distribution is a formula of the type $e^{-x^2}$.
A normal distribution is&mdash;as far as this program is concerned&mdash; a  Gaussian Distribution that has an intergral of 1.  A normal distribution follows the following function:

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

where $\mu$ represents the mean probalitiy value (the average or expected value) and $\sigma$ represents the, um, probability density. or something. The intergral between two values represents the probablilty that an event occours between those two values. For example, here is the chance that something falls between $a$ and $b$:

$$\int_{a}^{b}f(x)dx$$

Probablilties are continuous, so the chance of any specific value approaches 0.
# Some important equations 
**The Normal Probablilty Density Function**

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

**The Normal Cumulative Probablilty Function**

$$y = \int_{-\infty}^{x}f(z)dz$$

**The chance between $a$ and $b$**

$$\int_{a}^{b}f(x)dx$$

**The joint probability of two different normals ($f_1(x)$ and $f_2(x)$ ) and two different weights ($w_1$ and $w_2$)**

$w_1 + w_2$ = 1


graphed as a cumulative probability function

$$y = \int_{-\infty}^{x}f_1(z)w_1dz\int_{-\infty}^{x}f_2(z)w_2dz$$

graphed as a probablilty density function

$$y = \frac{d}{dx}\int_{-\infty}^{x}f_1(z)w_1dz\int_{-\infty}^{x}f_2(z)w_2dz dx$$

**joint probability for $n$ curves ( $f_1(x), f_2(x) ... f_{n-1}(x), f_n(x)$ ) and weights ( $w_1, w_2...w_{n-1}, w_n$ )**

$$ w_1 + w_2 ... + w_{n-1} + w_n = 1$$

$$\frac{d}{dx}\int_{-\infty}^{x}f_1(z)w_1dz\int_{-\infty}^{x}f_2(z)w_2dz ... \int_{-\infty}^{x}f_{n-1}(z)w_{n-1}dz\int_{-\infty}^{x}f_n(z)w_ndz dx$$
