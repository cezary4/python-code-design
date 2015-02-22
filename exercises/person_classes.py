# Plain old Person class
class Person(object):
    pass


# Class with a method that takes parameters.
# Not super useful beyond namespacing.
class PersonNamespace(object):

    def full_name(self, first_name, last_name):
        return first_name + " " + last_name

# Class with an inheritable method
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
        # In this case, we're calling __init__ on PersonWithInit in order to add the 
        # first_name and last_name attributes to our instance.

        # More details here:
        # https://docs.python.org/2/library/functions.html#super
        # https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        super(CandidateAdvanced, self).__init__(first_name, last_name)
        self.party = party

    def name_and_party(self):
        return self.full_name() + " (%s)" % self.party

if __name__ == '__main__':
    # Not much going on here
    p = Person()
    p.first_name = "Jane"
    p.last_name = "Smith"
    print "Person.first_name: %s" % p.first_name
    print "Person.last_name: %s"  % p.last_name
    print

    # Still not very useful beyond namespacing purposes
    p2 = PersonNamespace()
    print "PersonWithMethod.full_name: %s" % p2.full_name("Jane", "Smith")
    print

    # Inheritance is where classes start to shine.  Look ma, no args!!
    p3 = PersonWithInit('Jane', 'Smith')
    print "PersonWithInit.full_name (inherited method): %s" % p3.full_name() # Note we've inherited full_name from PersonWithMethod
    print

    cand = CandidateBasic('Jane', 'Smith', 'IND')
    print "CandidateBasic.full_name (inherited method): %s" % cand.full_name()
    print "CandidateBasic.party: %s" % cand.party
    print

    # A more complex example of inheritance
    cand2 = CandidateAdvanced('Jane', 'Smith', 'IND')
    print "CandidateAdvanced.full_name (inherited method): %s" % cand2.full_name()
    print "CandidateAdvanced.name_and_party (custom method): %s" % cand2.name_and_party()
    print
    