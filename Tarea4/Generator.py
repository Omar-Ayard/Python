def Pairs(*args):
    for value in args:
        if value % 2 == 0:
            yield value

for value in Pairs(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):
    print(value)