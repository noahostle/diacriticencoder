
inp = input('enter input string >> ')

sli = input("enter index(es) of character to diacritic (csv) >> ")

slis = None

if (',' in sli):
	slis = [int(i)-1 for i in sli.split(',')]
else:
	sli=int(sli)-1


pln = input("enter message to encode in diacritics >> ")

enc = ' '.join(format(ord(c), '08b') for c in pln)


cph=''
for x in enc:
	if x=='1':
		cph+='\u0332'
	elif x=='0':
		cph+='\u0331'
	else:
		cph+='\u0323'


if slis!=None:
	slis.sort()
	fmt=[None] * len(slis)
	inp=list(inp)
	print(str(len(pln))+" "+str(len(slis)))

	perletter=len(pln)//len(slis)
	remainder = len(pln)%len(slis)

	for y in range(0, len(slis)):
		if remainder > 0:
			n = (perletter+1)*9
			remainder-=1
		else:
			n = (perletter)*9
		try:
			fmt[y] = inp[slis[y]]+cph[:n]
		except:
			fmt[y] = inp[slis[y]]+cph[:9]
		
		cph=cph[n:]

		print(f"round {y}, setting inp[{slis[y]}] to {ascii(fmt[y])}")
		inp[slis[y]]=fmt[y]

	print(''.join(inp))

else:

	beg = inp[:sli]
	cha = inp[sli]
	end = inp[sli+1:]
	print(beg+cha+cph+end)

