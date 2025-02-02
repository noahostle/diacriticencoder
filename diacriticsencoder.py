import math
ye = input("Corny mode (y) or regular mode (n) >> ")
seven = input("Seven bit ascii mode (y/n) >> ")
shrtrascii=("y" in seven)

if "y" in ye:
	one='\u0329'
	zero='\u0325'
else:
	one='\u0332'
	zero='\u0330'

separator='\u0323'

inp = input('enter input string >> ')

sli = input("enter index(es) of character to diacritic (csv), or -1 for all >> ")

slis = None

if (',' in sli):
	slis = [int(i)-1 for i in sli.split(',')]
elif sli=='-1':
	slis = [j for j, c in enumerate(inp) if not c.isspace()]
else:
	sli=int(sli)-1


pln = input("enter message to encode in diacritics >> ")

bytez = '07b' if shrtrascii else '08b'
enc = ' '.join(format(ord(c), bytez) for c in pln)


cph=''
for x in enc:
	if x=='1':
		cph+=one
	elif x=='0':
		cph+=zero
	else:
		cph+=separator


#cph+=separator
#optional ^

if slis!=None:
	slis.sort()
	fmt=[None] * len(slis)
	inp=list(inp)
	print(str(len(pln))+" "+str(len(slis)))

	ln = len(pln*(8 if shrtrascii else 9))
	quot=ln//len(slis)
	remainder=ln%len(slis)

	print(f"{quot} {remainder}")


	for y in range(0, len(slis)):
		if inp[slis[y]].lower() not in "abcdefghijklmnopqrstuvwxyz":
			print("can't put diacritics on symbol character")
			break

		n=0
		if remainder>0:
			n=1
			remainder-=1

		n += quot
		try:
			fmt[y] = inp[slis[y]]+cph[:n]
		except:
			fmt[y] = inp[slis[y]]+cph
		
		cph=cph[n:]

		print(f"round {y}, setting inp[{slis[y]}] to {ascii(fmt[y])}")
		inp[slis[y]]=fmt[y]

	print(''.join(inp))

else:

	beg = inp[:sli]
	cha = inp[sli]
	end = inp[sli+1:]
	print(beg+cha+cph+end)

