import md5
import string
text = '1a'
for s in string.printable:
	if md5.new(text+s).hexdigest().startswith("1"):
		print md5.new(text+s).hexdigest() , s