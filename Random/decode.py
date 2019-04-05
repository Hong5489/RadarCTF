f = open("flag.txt",'r')
text = f.read().split(".")
key = int(chr(int(text[-1]) - 49))
flag = text[:-1]
print ''.join([chr(int(f) + key) for f in flag])