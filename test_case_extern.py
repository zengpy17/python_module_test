from mtest.binary_op.operators import plus, minus, mult, div

if __name__ == '__main__':
    print(f"1-4/2+3*5 is {plus(minus(1,div(4,2)),mult(3,5))}")