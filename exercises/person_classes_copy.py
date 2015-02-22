# Exercises I worked through from Serdar's notes for Nicar 2015 Python class:
# https://github.com/zstumgoren/python-code-design/blob/master/exercises/person_classes.py


# Plain old Person class
# All you've done here is created a class with no instruction on how it's structured
# You have to give it attributes in your script
class Person(object):
	pass

	'''def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	'''

# Class with a method that takes parameters.
# Not super useful beyond namespacing.
# Here you also have to give it attributes in your script
class PersonNamespace(object):

	def full_name(self, first_name, last_name):
		return first_name + " " + last_name

# Class with an inheritable method:
class PersonWithMethod(object):

	def full_name(self):
		return self.first_name + " " + self.last_name

# Class that inherits a method (full_name) from
# its parent class (PersonWithMethod)
class CandidateBasic(PersonWithMethod):

	def __init__(self, first_name, last_name, party):
		self.first_name = first_name
		self.last_name = last_name
		self.party = party

# Class with initial data AND behavior
# We use the data in the method.
class PersonWithInit(PersonWithMethod):

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	#def full_name(self):
	#	return self.first_name + " " + self.last_name

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


if __name__ == '__main__':
	# Not much going on here
	p = Person()
	p.first_name = "Jane"
	p.last_name = "Smith"
	print("Person.first_name: %s" % p.first_name) 
	print("Person.last_name: %s" % p.last_name)
	print()

	# Still not very useful beyond namespacing purposes
	p2 = PersonNamespace()
	print("PersonWithMethod.full_name: %s" % p2.full_name("Jane","Smith"))
	print()

	# Inheritance is where classes start to shine.  Look ma, no args!!
	# Don't see how this is an inherited method without above fix -- point out to Serdar
	p3 = PersonWithInit("Jane","Smith")
	print("PersonWithInit.full_name (inherited method): %s" % p3.full_name())
	print()

	# Clearer example of inherited method ("full_name") at work:
	cand = CandidateBasic("Jane","Smith","IND")
	print("CandidateBasic.full_name (inherited method): %s" % cand.full_name())
	print("CandidateBasic.party: %s" % cand.party)
	print()

	# A more complex example of inheritance
	# One of the method called on the cand2 instance is inherited ("full_name") while the other ("name_and_party") is defined in the class
	# methods are called on specific instances, so no need to pass parameters -- i.e. leave the parentheses null
	cand2 = CandidateAdvanced("Jane", "Smith", "IND")
	print("CandidateAdvanced.full_name (inherited method): %s" % cand2.full_name())
	print("CandidateAdevanced.name_and_party (custom method): %s" % cand2.name_and_party())
	print()













	
