from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print  "If you don't want that, hit CTRL -C (^c)."
print  "If you do want that, hit RETURN."

raw_input("?")

print  "Opening the file.."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm goning to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n123\n123\n123\n123")
target.write(line2)
target.write("\n345")
target.write(line3)
target.write("\n567")

print "And finally,we close it."
target.close()

txt =open(filename)
print txt.read()