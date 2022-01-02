#add implementation
def add(x,y):
    return x+y
#subtract impleamenttaion
def subtract(x,y):
    return x-y      #on master branch
#multiply implemnentaion
def multiply(x,y):
    return x*y          #on bug456 branch
#divide implementation
def divide(x,y):
    if y==0:   #master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y 

def square(x):
    return x*x