"""
4. Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).
"""
def product(*parameters):
    product = 1
    for parameter in parameters:
        product *= parameter
    print(product)

product(1, 5, 4)