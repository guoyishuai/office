from sys import argv

script, user_nme = argv
prompt = '><'

print "Hi %s, I'm the %s script." %(user_nme,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_nme
likes = raw_input(prompt)

print "Where do you live %s?" % user_nme
lives = raw_input(prompt)

print "What kind of computer do you  have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r .Not sure where that is.
And you have a %r computer.Nice.
""" % (likes, lives, computer)
