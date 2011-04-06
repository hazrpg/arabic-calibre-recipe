# This is used to encode arabic characters to something python can use.
f = open("encode.txt", 'r')
i = f.readline()
print i
j = unicode(i, 'utf-8')
print j.__repr__()
