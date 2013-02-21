from math import exp

__author__ = 'Jervis Muindi'

def hello():
    print('hello world from idea 9')

def f(x,y,z):
    # x^2*y + exp(-z)
    return x*x*y + exp(-z)

def run_monte_carlo():
    x0 = 0
    x1 = 2

    y0 = -1
    y1 = 1

    z0 = 1
    z1 = 125

    # Exact ans computed here: http://goo.gl/FjS3a
    exact_ans = 1.471152
    sample_nos = [10 ** 2, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    for n in sample_nos:
        val = monte_carlo(n,x0,x1,y0,y1,z0,z1)
        error = abs(val - exact_ans)
        print "For N = %d, Value is %f. Error = %f" % (n, val, error)


def monte_carlo(n,x0,x1,y0,y1,z0,z1):
    """
    Peforms Monte-Carlo integration on a 3D function with the given bounds.
    'n' is the number of sampling to do in the integration
    """
    assert(n > 0)
    volume = cube_volume(x0,x1,y0,y1,z0,z1)
    total = 0
    for i in xrange(0,n,1):
        x = random.uniform(x0, x1)
        y = random.uniform(y0, y1)
        z = random.uniform(z0, z1)
        total += f(x,y,z)
    result = volume * (total / n)
    return result

def cube_volume(x0,x1,y0,y1,z0,z1):
    return abs(x0-x1) * abs(y0-y1) * abs(z0-z1)


def main():
    run_monte_carlo()

if  __name__ == '__main__':
    main()