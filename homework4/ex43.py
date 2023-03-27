#Create the following infinite generators:
#(a) iter_even(), producing even numbers (0, 2, 4, ...),
#(b) iter_odd(), producing odd numbers (1, 3, 5, ...),
#(c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).



def iter_even():   
    i = 0
    while True:
        yield i+2

def iter_odd():
     i = 1
    while True:
        yield i+2

def iter_power():