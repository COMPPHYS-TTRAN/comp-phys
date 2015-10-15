    
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

    b = 0
    g = 0 #count how many b and f there are 
    
    if sex == 'boy':
        b += 1
        names = boy_names 
        for n in bnames:
            yield n
            print 'Welcome boy dolphin named {:s}!.format(n)

    if sex == 'girl':
        g += 1
        names = girl_names 
        for n in gnames:
            yield n
            print 'Welcome girl dolphin named {:s}!'.format(n)

        
#after all this, save these into TWO separate files

gen_boy_names = generate_names('boy')
gen_girl_names = generate_names('girl')