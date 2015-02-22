# Introduction to classes and inherritance in Python
# This tutorial: http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/

class Pet(object):

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species

	def __str__(self):
		return "%s is a %s" % (self.name, self.species)

'''

polly = Pet("Polly", "Parrot")

# Two ways to print species for the pet:

# Call method on the class and pass the instance "polly"
print("Polly is a %s" % Pet.getSpecies(polly))

# Won't work if you don't pass an instance:
#print("Polly is a %s" % Pet.getSpecies())

# Or call the method on the insteance "polly" in which case you don't need to pass anything:
print("Polly is a %s" % polly.getSpecies())

'''

# Defining a subclass
# Dog and Cat are subclasses of pets:

class Dog(Pet):

	def __init__(self, name, chases_cats):
		Pet.__init__(self, name, "Dog")
		self.chases_cats = chases_cats

	def chasescats(self):
		return self.chases_cats

class Cat(Pet):

	def __init__(self, name, hates_dogs):
		Pet.__init__(self, name, "Cat")
		self.hates_dogs = hates_dogs

	def hatesdogs(self):
		return self.hates_dogs

# Dog is a subclass of Pet because mister_pet is a pet but not a dog, while mister_dog is both a pet AND a dog:
# isinstance is a function that tells you whether a particular instance belongs to a class

'''
>>> isinstance(mister_pet, Pet)
True
>>> isinstance(mister_pet, Dog)
False

>>> isinstance(mister_dog, Pet)
True
>>> isinstance(mister_dog, Dog)
True
'''

# That means you can call Pet methods on mister_dog but but can't call dog methods on mister_pet

# Passing instances to strings:
# Remember that Python 3.4 is CaSe SeNsItIve

'''
print("%s chases cats: %s" % (fido.getName(), fido.chasescats()))
print("%s hates dogs: %s" % (fluffy.getName(), fluffy.hatesDogs()))
'''

# Further documenation:
# https://docs.python.org/2/tutorial/classes.html

