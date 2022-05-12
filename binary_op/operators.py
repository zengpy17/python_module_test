from python_module_test.unary_op.operators import minus as u_minus

def plus(a,b):
    return a+b

def minus(a,b):
    return plus(a, u_minus(b))

def mult(a,b):
    return a*b

def div(a,b):
    return a/b