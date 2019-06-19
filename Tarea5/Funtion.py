def myFuntion(*list,**dict):
    for v in list:
        print(v)

    for k,v in dict.items():
        print("The Key is: "+str(k)+" \nThe Value is: "+str(v))



myFuntion(1,2,3,4,5,6, a='A',b='B', c="C")
