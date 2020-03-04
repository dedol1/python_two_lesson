from sys import argv
script, uname = argv

pointer = ">> "

print "Hello %s, welcome to %s" % (uname, script)
print """ here is what the game is all about\n
 *****************************************\n
 we will ask you a question and then you have to answer honestly
 """

print "Are you a girl %s?" % uname
gender = raw_input(pointer)

if (gender == yes):
    print "you're are a girl"
else:
    print "you're a boy"




