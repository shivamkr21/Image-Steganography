from PIL import Image  
def genData(data): 
		newd = [] 		
		for i in data: 
			newd.append(format(ord(i), '08b'))                              #converting number in binary and appending in list1
		#print(newd)		
		return newd 
def modPix(pix, data): 
	datalist = genData(data)                        #list of binary data to be hide
	lendata = len(datalist) 
	imdata = iter(pix) 
	for i in range(lendata): 
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]] 
		#print('\n')
		#print("Original pixels\t")
		#print(pix) 
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0):                    #number is odd and binary data to be encoded is[0]  
				if (pix[j]% 2 != 0): 										
					pix[j] -= 1
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1		
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1
		pix = tuple(pix)
		#print("modified pixel\t")
		#print(pix)
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 
def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 	
	for pixel in modPix(newimg.getdata(), data): 
		#print("putting pixel at location ",x,",",y,"\t",pixel) 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1	
def encode(): 
	img = input("Enter image name(with extension): ") 
	image = Image.open(img, 'r') 
	
	data1 = input("Enter data to be encoded : ") 
	if (len(data1) == 0): 
		raise ValueError('Data is empty')
	data2=input("Enter decoding password : ")
	data=data1+data2 		
	newimg = image.copy() 
	encode_enc(newimg, data) 
	newimg.save("newimg.png", 'PNG') 
	print("Image saved with name \"newimg.png\"")
def decode(): 
	img = input("Enter image name(with extension) :") 
	image = Image.open(img, 'r') 
	x,y=0,0
	data = '' 
	imgdata = iter(image.getdata()) 
	
	while (True): 
		pixels = [value for value in imgdata.__next__()[:3] +
									imgdata.__next__()[:3] +
									imgdata.__next__()[:3]] 
		# string of binary data 
		binstr = '' 
		
		for i in pixels[:8]: 
			if (i % 2 == 0): 
				binstr += '0'
			else: 
				binstr += '1'
				
		data += chr(int(binstr,2)) 
		if (pixels[-1] % 2 != 0): 
			check(data)			
			return data 
	

def check(data):
	a=data
	flag=True
	while(flag):
		password=input("Enter decoding password :")
		lenp=len(password) 
		passw=''
		for i in range((len(a)-lenp),len(a)):
			passw+=str(a[i])
		if(passw==password):
			flag=False
			print("Decode text is \t")
			for i in range(len(a)-lenp):
				print(a[i],end="")
			print("\n")
		else: 
			#image1 = Image.open('wtf.jpg', 'r')
			#image1.show()
			print("INCORRECT PASSWORD")

def main(): 
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n 2. Decode\n")) 
	if (a == 1): 
		encode() 
	elif (a == 2): 
		b=decode() 
	else: 
		raise Exception("Enter correct input") 
if __name__ == '__main__' : 
	main() 
