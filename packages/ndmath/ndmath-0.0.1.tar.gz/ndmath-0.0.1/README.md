# ndmath

ndmath is a Python library for N-dimensional complex step differentiation and Newton's method.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ndmath.

```bash
pip install ndmath
```

## Examples

Calculating the Jacobian at a point:
```python
import ndmath

ndmath.complexGrad(lambda x : x[0]**2+x[1], [1,2]) # returns array([2., 1.])
ndmath.finiteGrad(lambda x : x[0]**2+x[1], [1,2], 10**-7) # returns array([2.0000001, 1.])
```
Using the root-finding Newton's method:
```python
def func(x):
    return [(x[1]-3)**2+x[0]-5, 2*x[1]+x[0]**3]

def fprime(x):
    return ndmath.complexGrad(func, x)

x0 = [0,0] #initial estimate

ndmath.nDimNewton(func, x0, fprime) # returns array([-1.02890183,  0.54461778])
```

## Contributing
Pull requests are welcome. Feel free to open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)