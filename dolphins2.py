#### class in this loop
#now that you have couple, 
#creation happens
#a year passes
#dolphin instantiations and edits will be made in this loop
#when finishes, will go back up to boy loop

import random
import pdb

import urllib2
import re


matchstring = '.*<td><span class="a nameDetails">.*</span></td>'

    #BOYS
pgn = 1
boys_temp = []
boys = []

while pgn <= 20: #while there are less than 700 names, keep looking for names
    url_boys = 'http://www.prokerala.com/kids/baby-names/boy/page-' + str(pgn) + '.html'

    dir_path = "/Users/labuser/comp-phys/"
    filenm_boys = dir_path + 'names/boys_names.html'                

    infile_boys = urllib2.urlopen(url_boys)
    lines_boys = infile_boys.read()  
    infile_boys.close()

        #has just create file object that exist as long as python session exists
    boys_temp = re.findall(matchstring, lines_boys)
    boys += boys_temp

    pgn += 1

bnames = []    
for n in boys:  
    name = n.lstrip('.*<td><span class="a nameDetails">').rstrip('</span></td>')
    bnames.append(name)
    #GIRLS
pgn = 1
girls_temp = []
girls = []

while pgn <= 20: #while there are less than 700 names, keep looking for names
    url_girls = 'http://www.prokerala.com/kids/baby-names/girl/page-' + str(pgn) + '.html'

    dir_path = "/Users/labuser/comp-phys/"
    filenm_girls = dir_path + 'names/girls_names.html' 

    infile_girls = urllib2.urlopen(url_girls)
    lines_girls = infile_girls.read()  
    infile_girls.close()

        #has just create file object that exist as long as python session exists
    girls_temp = re.findall(matchstring, lines_girls)
    girls += girls_temp

    pgn += 1

gnames = []
for n in girls:  
    name = n.lstrip('.*<td><span class="a nameDetails">').rstrip('</span></td>')
    gnames.append(name)

random.shuffle(bnames)
random.shuffle(gnames)
    
def generate_names(sex):

        #reading files and closing files
        #has extracted information
        #proceeding to use regular expression to extract names
        #uses findall() method because it saves things in list
        #should return list to use for generator

    if sex == 'boy':
        
#             for n in bnames:
#                 yield n
#                 #print 'Welcome boy dolphin named {:s}!'.format(n)
        
            #for n in bnames:
        i = 10
        k = 0
        while i < 11:
            middle = random.randint(0, 1000000)
            n = bnames[k % 700]
            yield n + str(middle)
            k += 1
                
                
    if sex == 'girl':
        
#             for n in gnames:
#                 yield n
#                 #print 'Welcome boy dolphin named {:s}!'.format(n)
        
            #for n in gnames:
        i = 10
        k = 0
        while i < 11:
            middle = random.randint(0, 1000000)
            n = gnames[k % 700]
            yield n + str(middle)
            k += 1
    #after all this, save these into TWO separate files

gen_boy_names = generate_names('boy')
gen_girl_names = generate_names('girl')


    #the beginning of each trial/simulation begins with two dolphins of each sex 

# for i in range(300):
#     boy_dolphin = gen_boy_names.next()

# for i in range(300):
#     girl_dolphin = gen_girl_names.next()

    #now that we have generator, start tying it into class Dolphins
    #class Dolphins cannot be called until two dolphins have sex
    #this will be the initial condition always

class Dolphins:

    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.death = random.gauss(mu = 35, sigma = 5 )
        self.banged = 0 #time since dolphin last had sex

    #def mean(self):
            #print 'oops'

    #def standev(self):
            #print 'i did it again'

    def bang(self, Dolphin_Bang):
            #four stipulations
            #answers: can THIS whale have sex?

        if (self.age < 8) or (Dolphin_Bang.age < 8):
            return False # "Where is puberty really"
                        #dolphins too young
        
        if abs(self.age - Dolphin_Bang.age) >= 10:
            return False # "'She's too young for you, brah"
                            #not within age range

        if (Dolphin_Bang.mother, Dolphin_Bang.father) == (self.mother, self.father):
            return False #'LUKE AND LEIA'
                            #related

        if (self.sex == Dolphin_Bang.sex):
            return False # 'No gay dolphins'
                            #can't procreate...literally
        
        if (self.banged < 6):
            return False #cannot procreate
        
        if (Dolphin_Bang.banged < 6):
            return False 
        
        else:
            return True

    def dead(self):
        if self.age == int(self.death):
            return True
        else:
            return False

        #first: can they bang
        #second: they bang and have baby
        #third: update bang records 

    def update(self):
        self.banged += 1 #the years since dolphin has had sex 
        self.age += 1   
            
gen_boy_names = generate_names('boy')
gen_girl_names = generate_names('girl')

#procreation function outside class Dolphin
  
boy_alive = []
girl_alive = [] 

def creation(mother, father):
    #live_dolphins = 4 #initial condition
    #print mother.bang(father)
    if mother.bang(father) == True: 
        mother.banged = 0
        father.banged = 0
        
        sex = random.choice(['boy', 'girl'])
        if sex == 'boy': 
            boy_gen = gen_boy_names.next() #gen names
            boy_dolph_baby = Dolphins(boy_gen, sex, mother, father)
            boy_alive.append(boy_dolph_baby) #list appends instantiations of baby dolphins
            return boy_dolph_baby           #length of this list is number of living boy/girl dolphins
        else:
            girl_gen = gen_girl_names.next()
            girl_dolph_baby = Dolphins(girl_gen, sex, mother, father)
            girl_alive.append(girl_dolph_baby)
            return girl_dolph_baby
    else:
        return 'NO BABIES.'
        
Terrence = Dolphins('Terrence', 'boy', 'Laura', 'Si')
Tyrone = Dolphins('Tyrone', 'boy', 'Karen', 'Smith')
Terry = Dolphins('Terry', 'girl', 'Loan', 'Yes')
Tina = Dolphins('Tina', 'girl', 'Linda', 'Bob')
boy_alive.append(Terrence)
boy_alive.append(Tyrone)
girl_alive.append(Terry)
girl_alive.append(Tina)
#print 'jello'
    
def main():
    for t in range(1, 11):
        print 'Trial No. ', t
        live_dolphins = 4
        for years in range(151): #iterate 150 years
                #needs "official documents" in this one
                #generator needs to come before male/female nested loop
                #years will automatically update--does not need to do that here
            if years == int(25):
                print 'Entering year 25 with ', live_dolphins, ' dolphins, with 0 breeding.'
            if years == int(50):
                print 'Entering year 50 with ', live_dolphins, ' dolphins, with 0 breeding.'
            if years == int(75):
                print 'Entering year 75 with ', live_dolphins, ' dolphins, with 0 breeding.'
            if years == int(100):
                print 'Entering year 100 with ', live_dolphins, ' dolphins, with 0 breeding.'
            if years == int(125):
                print 'Entering year 125 with ', live_dolphins, ' dolphins, with 0 breeding.'
            if years == int(150):
                print 'Entering year 150 with ', live_dolphins, ' dolphins, with 0 breeding.'

            for male in boy_alive:
                male.update()
                if male.dead() == True:
                    live_dolphins -= 1
                    boy_alive.remove(male)
                    #live_dolphins -= 1
                    #return boy_alive
                    #return live_dolphins

            for female in girl_alive:
                female.update()
                if female.dead() == True:
                    live_dolphins -= 1
                    girl_alive.remove(female)
                    #return girl_alive
                    #return live_dolphins

            for male in boy_alive: #nested for loop max coupling
                #pdb.set_trace()
                #when finished with girl loop, will go back up here

                for female in girl_alive:
                        #class in this loop
                        #now that you have couple, 
                        #creation happens
                        #a year passes
                        #dolphin instantiations and edits will be made in this loop
                        #when finishes, will go back up to boy loop

                        #print male.name, female.name
                        #print male.age, female.age
                        baby = creation(female, male)

                        if isinstance(baby, Dolphins):
                            if baby.sex == 'girl':
                                girl_alive.append(baby)
                            if baby.sex == 'boy':
                                boy_alive.append(baby) 
                            live_dolphins += 1   
main()
                          
