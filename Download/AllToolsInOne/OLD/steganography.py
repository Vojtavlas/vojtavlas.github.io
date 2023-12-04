black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
import png
import base64
from tkinter import filedialog as fd
PROMPT = f"""
{red}Welcome to basic steganography. Please choose:

{red}1. To encode a message into an image
{red}2. To decode an image into a message
{red}q. to exit
"""

ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"


def encode_message_as_bytestring(message):
	b64 = message.encode("utf8")
	bytes_ = base64.encodebytes(b64)
	bytestring = "".join(["{:08b}".format(x) for x in bytes_])
	bytestring += ENDOFMESSAGE
	return bytestring


def get_pixels_from_image(fname):
	img = png.Reader(fname).read()
	pixels = img[2]
	return pixels


def encode_pixels_with_message(pixels, bytestring):
	'''modifies pixels to encode the contents from bytestring'''

	enc_pixels = []
	string_i = 0
	for row in pixels:
		enc_row = []
		for i, char in enumerate(row):
			if string_i >= len(bytestring): 
				pixel = row[i]
			else:
				if row[i] % 2 != int(bytestring[string_i]):
					if row[i] == 0:
						pixel = 1
					else:
						pixel = row[i] - 1
				else:
					pixel = row[i]
			enc_row.append(pixel)
			string_i += 1

		enc_pixels.append(enc_row)
	return enc_pixels


def write_pixels_to_image(pixels, fname):
	png.from_array(pixels, 'RGB').save(fname)


def decode_pixels(pixels):
	bytestring = []
	for row in pixels:
		for c in row:
			bytestring.append(str(c % 2))
	bytestring = ''.join(bytestring)
	message = decode_message_from_bytestring(bytestring)
	return message


def decode_message_from_bytestring(bytestring):
	bytestring = bytestring.split(ENDOFMESSAGE)[0]
	message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
	message = base64.decodebytes(message).decode("utf8")
	return message


def main():
	print(PROMPT)
	user_inp = ""
	while user_inp not in ("1", "2", "q"):
		user_inp = input(f"{red}Your choice:{white} ")

	
	if user_inp == "1":
		in_image = fd.askopenfilename()
		in_message = input(f"{red}Please enter the message to encode:{white} ")

		print(f"{red}-ENCODING-")
		pixels = get_pixels_from_image(in_image)
		bytestring = encode_message_as_bytestring(in_message)
		epixels = encode_pixels_with_message(pixels, bytestring)
		write_pixels_to_image(epixels, in_image + "-enc.png")

	elif user_inp == "2":
		in_image = fd.askopenfilename()
		print(f"{red}-DECODING-")
		pixels = get_pixels_from_image(in_image)
		print(decode_pixels(pixels))

if __name__ == "__main__":
	main()