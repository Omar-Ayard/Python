
class Chicken:
    total=0

    def __init__(self,name,specie):
        self.name=name
        self.specie=specie
        self.eggs=0

    def lay_egg(self):
        self.eggs+=1
        Chicken.total+=1


gallina1=Chicken("Petra","Gallinas pintas")
gallina2=Chicken("Rebeca","Culecas")

gallina1.lay_egg()
gallina1.lay_egg()
gallina2.lay_egg()

print("*** 1 ***")
print("La gallina: "+str(gallina1.name)+" tiene: "+str(gallina1.eggs)+" huevos ")
print("La gallina: "+str(gallina2.name)+" tiene: "+str(gallina2.eggs)+" huevos ")
print("En la Granja hay: "+str(Chicken.total)+" Huevos \n")

gallina2.lay_egg()
gallina2.lay_egg()
gallina2.lay_egg()
gallina1.lay_egg()

print("*** 2 ***")
print("La gallina: "+str(gallina1.name)+" tiene: "+str(gallina1.eggs)+" huevos ")
print("La gallina: "+str(gallina2.name)+" tiene: "+str(gallina2.eggs)+" huevos ")
print("En la Granja hay: "+str(Chicken.total)+" Huevos \n")