c=33.40
values=[1,'c',45,67,'w','j','o',33,'Hello',28,"This is a String",c]

def chars(value):
    try:
        value=int(value)
    except ValueError:
        return True #Filter retorna verdadero si es el valor que se pretende filtra

result=list(filter(chars,values))

print(result)