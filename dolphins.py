import random
import pdb

class Dolphins:
    
    def __init__(self, name, sex, mother, father, age = 0, year = 0):
        self.name = name
        self.sex = sex
        self.age = age #key word variable for age b/c it changes
        self.mother = mother
        self.father = father
        self.death = random.gauss(mu = 35, sigma = 5) 
        self.year = year #key word variable for year b/c same reason
        
        print 'A ' + str(self.sex) + ' dolphin named ' + str(self.name) + ' is born!!!!!! ' 

    def __str__(self):
        return 'A ' + str(self.sex) + ' dolphin named ' + str(self.name) + ' is born!!!!!! ' 
    
    def bang(self, Dolphin_Bang):
        #four stipulations
        if (self.age < 8) or (Dolphin_Bang < 8):
            return False # "Where is puberty really"
                        #dolphins too young
        
        if abs(self.age - Dolphin_Bang.age) >= 10:
            return False # "'She's too young for you, brah"
                        #not within age range
        
        if (Dolphin.mother, Dolphin.father) == (self.mother, self.father):
            return False #'LUKE AND LEIA'
                        #related
        
        if (self.sex == Dolphin_Bang.sex):
            return False # 'No gay dolphins'
                        #can't procreate...literally
        
        else:
            return True
        
    def update(self):
        self.year += 1
        self.age += 1
