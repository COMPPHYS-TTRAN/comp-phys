'''
#HW04
#Terry Tran
#Partner: Jacob Baca

'''

import datetime as dt
import random
import pdb

class Whale:
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex
		self.life = dt.datetime.now()
		print 'A ' + str(self.sex) + ' whale named ' + str(self.name) + ' is born!!!!!! ' + str(dt.datetime.now() - self.life)

	def age(self):
		#pdb.set_trace()
		self.age = dt.datetime.now() - self.life
		return self.age

	def __str__(self):
		return 'A ' + str(self.sex) + ' whale named ' + str(self.name) + ' is born!!!!!! ' + str(dt.datetime.now() - self.life)

	def sing(self):
		self.sing = sing
        	print '\a \a \a \a \a'

names = ['RKelly', 'Usher', 'Popo', 'John,', 'Tyrone', 'Albs', 'Drake', 'Scar', 'Simba', 'Tutenkhamun', \
         'Nala','Kate', 'Orca', 'Lily', 'Tigerlily', 'Wendy', 'Sukhi', 'No', 'TTTT', 'Mina']

names_instance = []

for n in names:
	bg = ['boy', 'girl']
	random.shuffle(bg)
	gbbg = bg[0]
	x = Whale(n, gbbg)
	names_instance.append(x)

