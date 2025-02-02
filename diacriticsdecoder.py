inp = input("enter diacritics encoded string >> ")
inter=''


for x in list(inp):
	if ord(x)>256:
		if x=='\u0332' or x=="\u0329":
			inter+='1'
		elif x=='\u0330' or x=="\u0325":
			inter+='0'
		else:
			inter+=' '


print(''.join(chr(int(b, 2)) for b in inter.split()))