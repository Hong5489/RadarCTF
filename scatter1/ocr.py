from PIL import Image
import pytesseract
for i in range(1,577):
	image = Image.open(str(i) + ".jpg")
	newImage = image.crop(box=(10,10,130,130))
	text = pytesseract.image_to_string(newImage,config='--psm 10')
	print text,