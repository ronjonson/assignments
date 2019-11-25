import sys, barcode
from barcode.writer import ImageWriter
from PIL import Image


def arg_check(args): #checks command line arguments for a filename
	length = len(args)
	if length < 2:
		return False
	else:
		return True

def main():
	args = sys.argv
	if arg_check(args) is False: #if there is no filename, the default name is sample.jpeg
		filename = "sample"
	else:
		filename = args[1]

	code39 = barcode.get_barcode_class('code39')
	text = input("type text here: ") #asks for text to convert
	bar = code39(text, writer = ImageWriter(), add_checksum = False)
	full = bar.save(filename)

	print("your barcode is saved as "+filename+".png")

	img = Image.open(filename + '.png')
	img.show()
if __name__ == '__main__':
	main()