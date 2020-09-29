class partyAnimal :
    x=0
    name=""
    def party(self,z) :
        self.name = z
        print(self.name,'is in')

    def party2(self) :
        self.x = self.x + 1
        print('is there',self.x)    

class Gamers(partyAnimal) :                     #class gamers extends partyAnimal i.e gamers everything of partyanimal plus its own
    ign = ""
    def game(self,zz) :
        self.ign = zz
        print('ign is : ',self.ign)        

an = partyAnimal()
an.party('anuj')
an.party2()

ann = Gamers()
ann.game('souless')
an.party2()
