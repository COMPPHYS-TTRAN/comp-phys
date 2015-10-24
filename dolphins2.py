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

def generate_names(sex):

        #reading files and closing files
        #has extracted information
        #proceeding to use regular expression to extract names
        #uses findall() method because it saves things in list
        #should return list to use for generator

    matchstring = '.*<td><span class="a nameDetails">.*</span></td>'

        #BOYS
    pgn = 1
    boys_temp = []
    boys = []

    while pgn <= 3: #while there are less than 700 names, keep looking for names
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

    while pgn <= 3: #while there are less than 700 names, keep looking for names
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

    if sex == 'boy':
            #names = boy_names 
        for n in bnames:
            yield n
                #print 'Welcome boy dolphin named {:s}!'.format(n)

    if sex == 'girl':
            #names = girl_names 
        for n in gnames:
            yield n
                #print 'Welcome girl dolphin named {:s}!'.format(n)


    #after all this, save these into TWO separate files

gen_boy_names = generate_names('boy')
gen_girl_names = generate_names('girl')


    #the beginning of each trial/simulation begins with two dolphins of each sex 

for i in range(50):
    boy_dolphin = gen_boy_names.next()

for i in range(50):
    girl_dolphin = gen_girl_names.next()

    #now that we have generator, start tying it into class Dolphins
    #class Dolphins cannot be called until two dolphins have sex
    #this will be the initial condition always

class Dolphins:

    def __init__(self, name, sex, mother, father, age = 0, year = 0, bangfreq = 0, live_dolphin = 4):
        self.name = name
        self.sex = sex
        self.age = age #key word variable for age b/c it changes
        self.mother = mother
        self.father = father
        self.death = random.gauss(mu = 35, sigma = 5) 
        self.year = year #key word variable for year b/c same reason
        self.bangfreq = bangfreq
        self.live_dolphin = live_dolphin

    #def mean(self):
            #print 'oops'

    #def standev(self):
            #print 'i did it again'


    def bang(self, Dolphin_Bang):
            #four stipulations
            #answers: can THIS whale have sex?

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

    def dead(self):
        if self.age == self.death:
            return True
            lst_live_dolphins.remove(self.name)
            live_dolphins -= 1
        else:
            print 'Not dead yet.'

        #first: can they bang
        #second: they bang and have baby
        #third: update bang records 

    def update():
        self.year += 1 
        self.age += 1        

    #four initial instantiations of dolphins

gen_boy_names = generate_names('boy')
gen_girl_names = generate_names('girl')

    #procreation function outside class Dolphin
  
boy_alive = []
girl_alive = [] 

def creation(mother, father):
    live_dolphins = 4 #initial condition
    if Dolphins.bang == True:
        sex = random.random([boy, girl])
        if sex == 'boy': 
            boy_gen = gen_boy_names.next() #gen names
            boy_dolph_baby = Dolphins(boy_gen, sex, mother, father)
            boy_alive.append(boy_dolph_baby) #list appends instantiations of baby dolphins
                                            #length of this list is number of living boy/girl dolphins
        else:
            girl_gen = gen_girl_names.next()
            girl_dolph_baby = Dolphins(girl_gen, sex, mother, father)
            girl_alive.append(girl_dolph_baby)

        mother.bang_freq += 1
        father.bang_freq += 1
        live_dolphins += 1 #when dolphin born
    else:
        print 'NO BABIES.'

        
Terrence = Dolphins('Terrence', 'boy', 'Laura', 'Si')
Tyrone = Dolphins('Tyrone', 'boy', 'Karen', 'Smith')
Terry = Dolphins('Terry', 'girl', 'Loan', 'Yes')
Tina = Dolphins('Tina', 'girl', 'Linda', 'Bob')
boy_alive.append('Terrence')
boy_alive.append('Tyrone')
girl_alive.append('Terry')
girl_alive.append('Tina')
#print 'jello'


def main():

    for years in range(151): #iterate 150 years
            #needs "official documents" in this one
            #generator needs to come before male/female nested loop
            #years will automatically update--does not need to do that here

        live_dolphins = 4 
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
            print 'Entering year 150 with ', live_dolphins, ' dolphins,with 0 breeding.'
            
            for male in boy_alive: #nested for loop max coupling
                #pdb.set_trace()
                #when finished with girl loop, will go back up here
                #then say 'Entering year __ blah blah blah

                for female in girl_alive:
                        #class in this loop
                        #now that you have couple, 
                        #creation happens
                        #a year passes
                        #dolphin instantiations and edits will be made in this loop
                        #when finishes, will go back up to boy loop
                        
                        baby = creation(female, male)
                        
                        if isinstance(baby, Dolphins):
                            lst_dolphins_dolphins.append(baby.name)
                            live_dolphin += 1
                            
                            
main()