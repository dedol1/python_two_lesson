#just like the script with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# alternative way of writing the code up there

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)


#taking one argument

def print_one(arg1):
    print "arg1: %r" % arg1

# taking no argument

def print_none():
    print "I got nothing"


print_two("samuel", "afotey")
print_two_again("samuel", "afotey")
print_one("First!")
print_none()

