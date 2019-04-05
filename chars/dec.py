f = open('flag.txt','r')
text = f.read()
print text
print text.replace('\r\n','').replace("R",'')