class Perro: 
    edad = 34
    def __init__(self,name): 
        self.name= name 
        self.tricks = [] 
        
    def add_tricks(self,new_trick): 
        self.tricks.append(new_trick) 
        
pet1 = Perro("peter") 

pet1.add_tricks("sit")
print(pet1.tricks)
pet1.add_tricks("comeback") 
print(pet1.tricks)