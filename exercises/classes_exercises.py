# Plain old Person class

#class Person(object):
#	pass

# Class with a method that takes parameters.
# Not super useful beyond namespacing.
# Namespacing is a way of keeping track of things in python (variables, instances)

class Person(object):

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def fname(self):
		return self.first_name 

	def lname(self):
		return self.last_name

	def full_name(self):
		return self.first_name + " " + self.last_name

	def __str__(self):
		return self.first_name + " " + self.last_name + " is a person."

# Candidate subclass

"""
class Candidate(object):

	def __init__(self, first_name, last_name, party):
		Person.__init__(self, first_name, last_name)
		self.party = party

	def __str__(self):
		return self.first_name + " " + self.last_name + " is a " + self.party + " candidate."

"""

# A better example of inherritance

class Candidate(object):

	def __init__(self, first_name, last_name, party):
		self.first_name = first_name
		self.last_name = last_name
		self.party = party

	def fname(self):
		return self.first_name 

	def lname(self):
		return self.last_name

	def full_name(self):
		return self.first_name + " " + self.last_name

	def the_party(self):
		return self.party

	def __str__(self):
		return self.first_name + " " + self.last_name + " is a " + self.party + " candidate."

# Democrats subclass:

class Democrats(Candidate): # <-- THIS IS HOW YOU CREATE A SUBCLASS!!

	def __init__(self, first_name, last_name, position):
		Candidate.__init__(self, first_name, last_name, "Democrat")
		self.position = position

	def __str__(self):
		return self.first_name + " " + self.last_name + " is a " + self.position + " " + self.party

''' So now all this code works:

>>> from exercises_copy import Person, Candidate, Democrats
>>> cezary = Democrats("Cezary", "Podkul", "Governor")

>>> cezary.fname()
'Cezary'

>>> cezary.lname()
'Podkul'

>>> cezary.full_name()
'Cezary Podkul'

>>> Candidate.the_party(cezary)
'Democrat'

>>> print(cezary)
Cezary Podkul is a Governor Democrat

# That's because I am an instance of both the Candidate class and Democrats subclass:

>>> isinstance(cezary, Democrats)
True
>>> isinstance(cezary, Candidate)
True

# Marta is not a Democrat:

>>> marta = Candidate("Marta", "Podkul", "Republican")
>>> print(marta)
Marta Podkul is a Republican candidate.

>>> isinstance(marta, Candidate)
True
>>> isinstance(marta, Democrats)
False

'''

### Another way to do inherrit, using the Super function ###

#Super: https://docs.python.org/2/library/functions.html#super

class Position(Candidate): # <-- THIS IS HOW YOU CREATE A SUBCLASS!!

	def __init__(self, first_name, last_name, party, position):
		super(Position, self).__init__(first_name, last_name, party)
		self.position = position

	def __str__(self):
		return self.first_name + " " + self.last_name + " is a " + self.position

''' It works - can define Position object and use Candidate methods:

>>> cezary = Position("Cezary", "Podkul", "Democrat","Governor")
>>> cezary.fname()
'Cezary'

>>> cezary.lname()
'Podkul'
>>> cezary.full_name()
'Cezary Podkul'
>>> print(cezary)
Cezary Podkul is a Governor
'''


# From Serdar's notes:

# Class with initial data AND behavior
# We use the data in the method.

class PersonWithInit(object):

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def full_name(self):
		return self.first_name + " " + self.last_name

# Class that blends data AND behavior
# inherited from a parent class (through the use of "super")
# with its own customized data AND behavor
class CandidateAdvanced(PersonWithInit):

	def __init__(self, first_name, last_name, party):
	# The built-in super function allows you to call methods on a parent class of the instance. 
	# In this case, we're calling __init__ on PersonWithInit in order to add the first_name and last_name attributes to our instance.
	# The difference is that here we just brought over some attributes (first and last name) and added a party attribute WITHOUT filling it in
		super(CandidateAdvanced, self).__init__(first_name, last_name)
		self.party = party

	def name_and_party(self):
		return self.full_name() + " %s" % self.party
		# What this does is it calls the full_name method on the person (self)
		# And then adds in a string where the string (%) is the party, as defined above

'''

if __name__ == '__main__':
	# Not much going on here
	p = Person(object)
	p.first_name = 'Jane'
	p.last_name = 'Smith'
	print("Person.first_name: %s" % p.first_name) 
	print("Person.last_name: %s" % p.last_name)

'''










	
