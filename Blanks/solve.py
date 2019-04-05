f = open("flag.txt",'r')
text = f.read().replace("\x09",'0').replace(" ",'1')
text = text + '01'
print hex(int(text,2))[2:-1].decode('hex')