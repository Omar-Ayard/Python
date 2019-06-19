from functools import reduce

values=[1,2,3,4,5]

def mult(acum,next):
    return acum*next

result=reduce(mult,values)

print("The result of the Multiplication is: "+str(result))
