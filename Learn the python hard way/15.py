from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
#print txt.read()

print "Type the filename again:"
file_again1 = raw_input(">")
txt1 = open(file_again1)
print txt1.read()
print txt1.read()
print txt1.read()
print txt1.read()


