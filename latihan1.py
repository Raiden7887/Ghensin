class Hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self,self.power)

    def diserang(self, lawan, power_lawan):
        damage = power_lawan/self.armor
        print("Damage " + str(damage))
        self.health -= damage
        if(self.health > 0):
            print("darah " + self.name + " tersisa " +str(self.health))
        elif(self.health > -1):
            print(self.name + " mati")
        elif(self.health <= -1):
            print("udah mati woy!!")
        
       

   

    def healthup(self, lawan):
        up = self.health/4
        lawan.health += up
        print( self.name + " memulihkan "+ lawan.name)
        print("darah " + lawan.name + str(lawan.health))

    def powerup(self, lawan):
        up = self.power/4
        lawan.power += up
        print( self.name + " ngebuff "+ lawan.name)
        print("power " + lawan.name +" meningkat " + str(lawan.power))




ganyu = Hero("ganyu ",10,20,5)
zhongli = Hero("zhongli",30,5,10)
kokomi = Hero("kokomi",15,10,5)
bennet = Hero("bennet",10,15,5)


ganyu.serang(zhongli)

zhongli.serang(ganyu)

kokomi.healthup(ganyu)

bennet.powerup(zhongli)

zhongli.serang(ganyu)
