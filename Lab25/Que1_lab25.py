class Car:
    def __init__(self,make,model,year,color):
        self.make= make
        self.model= model
        self.year= year
        self.color= color
        self.started= False
        self.speed = 0
        self.max_speed= 200

toyota_camry= Car('Toyota','Camry',2022,'Red')
print(toyota_camry)
        
    