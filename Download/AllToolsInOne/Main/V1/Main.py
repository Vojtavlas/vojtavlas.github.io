import hashid
import re
from tkinter import filedialog as fd
from rembg import remove
from PIL import Image
import time
import pyshorteners
import qrcode
import wifi_qrcode_generator as qr_wifi
from moviepy.editor import *
import string
import math
import requests
import base64
import png
import subprocess
import speedtest
import shutil
import os
from shutil import make_archive
from os import path 
from zipfile import ZipFile
from langdetect import detect
from forex_python.converter import CurrencyRates
import random
colors = [
    "\033[0;32m",  # GREEN
    "\033[0;34m",  # BLUE
       "\033[0;33m",  # YELLOW
    "\033[0;31m",  # RED
    "\033[0;37m"   # WHITE
]
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
RANDOM_COLOR = ""
def RANDOM():
    global RANDOM_COLOR
    RANDOM_COLOR = random.choice(colors)
    return RANDOM_COLOR
Options = f"""
{bred}[{yellow}1{bred}] {red} Background remover
{bred}[{yellow}2{bred}] {red} Url Shortener
{bred}[{yellow}3{bred}] {red} QR code generator
{bred}[{yellow}4{bred}] {red} MP4 to MP3
{bred}[{yellow}5{bred}] {red} Password generator
{bred}[{yellow}6{bred}] {red} Pythagoras theorem solver
{bred}[{yellow}7{bred}] {red} Currency converter
{bred}[{yellow}8{bred}] {red} Steganography
{bred}[{yellow}9{bred}] {red} Wifi speed test
{bred}[{yellow}10{bred}] {red}Zip generator
{bred}[{yellow}11{bred}] {red}YT video downloader(NOT DONE)
{bred}[{yellow}12{bred}] {red}Language detection
{bred}[{yellow}13{bred}] {red}Encrypt/Decrypt Text
{bred}[{yellow}14{bred}] {red}Password strenght meter
{bred}[{yellow}15{bred}] {red}Hash identifier
{bred}[{yellow}16{bred}] {red}Crypto currency price checker
{bred}[{yellow}17{bred}] {red}IP address information
{bred}[{yellow}18{bred}] {red}Subnet calculator
{bred}[{yellow}19{bred}] {red}Port scanner
{bred}[{yellow}20{bred}] {red}DNS lookup
{bred}[{yellow}21{bred}] {red}Url Unshortener
{bred}[{yellow}22{bred}] {red}Reverse IP Lookup
{bred}[{yellow}23{bred}] {red}Website info grabber
{bred}[{yellow}24{bred}] {red}Geo-location finder
{bred}[{yellow}25{bred}] {red}Email validator
{bred}[{yellow}26{bred}] {red}Phone number validator
{bred}[{yellow}27{bred}] {red}Credit card validator
{bred}[{yellow}35{bred}] {red}WhatsApp Web Scraper
{bred}[{yellow}36{bred}] {red}Google Search API
{bred}[{yellow}37{bred}] {red}Twitter scraper
{bred}[{yellow}38{bred}] {red}Instagram scraper
{bred}[{yellow}39{bred}] {red}Facebook scraper
{bred}[{yellow}40{bred}] {red}LinkedIn scraper
{bred}[{yellow}41{bred}] {red}Github scraper
{bred}[{yellow}42{bred}] {red}Reddit scraper
{bred}[{yellow}43{bred}] {red}Stackoverflow scraper
{bred}[{yellow}44{bred}] {red}Wikipedia scraper
{bred}[{yellow}45{bred}] {red}GitHub search
{bred}[{yellow}46{bred}] {red}Amazon product search
{bred}[{yellow}47{bred}] {red}YouTube search
{bred}[{yellow}48{bred}] {red}Netflix search
{bred}[{yellow}49{bred}] {red}IMDB movie search
{bred}[{yellow}50{bred}] {red}Spotify song search
{bred}[{yellow}00{bred}] {red}Quit
{white}
"""
OptionsHASH =f"""
{bred}[{yellow}1{bred}] {red}  MD5       | Hasher
{bred}[{yellow}2{bred}] {red}  SHA1      | Hasher
{bred}[{yellow}3{bred}] {red}  SHA256    | Hasher
{bred}[{yellow}4{bred}] {red}  SHA3      | Hasher
{bred}[{yellow}5{bred}] {red}  SHA384    | Hasher
{bred}[{yellow}6{bred}] {red}  SHA512    | Hasher
{bred}[{yellow}7{bred}] {red}  RIPEMD160 | Hasher
{bred}[{yellow}8{bred}] {red}  CRC32     | Hasher
{bred}[{yellow}9{bred}] {red}  KECCAK512 | Hasher
{bred}[{yellow}10{bred}] {red} CSHAKE256 | Hasher
"""
def bg_removal_success(file):
    output_file = file
    input_image = Image.open(file)
    output = remove(input_image)
    output.save(output_file)
    print(f"{red}Background removed successfully")
    input()
    os.system("cls")  # Clear terminal
def bg_removal(file):
    if file.lower().endswith('.png'):
        print(f"{red}File is an image")
        bg_removal_success(file)
    else:
        print(f"{red}File needs to be PNG to work")
def url_shortener(url):
    short_url = pyshorteners.Shortener().tinyurl.short(url)
    print(f"{red}The Shortened URL is:{yellow} ", short_url)
    input()
    os.system("cls")  # Clear terminal
def qrcodegenerator_url(url):
    img = qrcode.make(url)
    path_to_save_qr_code = input(f"{red}Name of the file:{white}") + ".png"
    img.save(path_to_save_qr_code)
    input()
    os.system("cls")  # Clear terminal
def qrcodegenerator_wifi():
    ssid = input(f'{red}Enter Wifi name:{white}')
    authentication_type = input(f"{red}Auth type (WPA/WEP):{white} ")
    if authentication_type in ["WPA", "WEP"]:
        password = input(f"{red}Enter Wifi password:{white}")
        qr_code = qr_wifi.wifi_qrcode(ssid, False, authentication_type, password)
        qr_code.make_image().save("wifi.png")
        input()
        os.system("cls")  # Clear terminal
def qrcodegenerator_text(text):
    img = qrcode.make(text)
    path_to_save_qr_code = input(f"{red}Name of the file:{white} ") + ".png"
    img.save(path_to_save_qr_code)
    input()
    os.system("cls")  # Clear terminal
def mp4_to_mp3(file):
    video = VideoFileClip(file)
    name = input(f"{red}Name of the final file:{white}") + ".mp3"
    video.audio.write_audiofile(name)
    input()
    os.system("cls")  # Clear terminal
def PasswordGenerator():
    try:
        length = int(input(f"{red}Length of the password:{white} "))
    except ValueError:
        print(f"{red}You didn't enter a number.")
        input()
        return
    print(f'''{red}Choose character set for password from these:
{bred}[{yellow}1{bred}]{red} Digits
{bred}[{yellow}2{bred}]{red} Letters
{bred}[{yellow}3{bred}]{red} Special characters
{bred}[{yellow}4{bred}]{red} Continue''')
    character_list = ""
    while True:
        try:
            choice = int(input(f"{red}Pick a number:{white} "))
        except ValueError:
            print(f"{red}You didn't enter a number.")
            input()
        if choice == 1:
            character_list += string.digits
        elif choice == 2:
            character_list += string.ascii_letters
        elif choice == 3:
            character_list += string.punctuation
        elif choice == 4:
            password = [random.choice(character_list) for _ in range(length)]
            print(f"{red}The random password is:{yellow}", "".join(password))
            input()
            os.system("cls")  # Clear terminal
            break
        else:
            print(f"{red}Please pick a valid option!")
def Pythagoras_theorem_solver():
    side = input(f"{red}Give the side you want to solve for (a, b, or c):{white} ")
    try:
        if side == "a":
            b = float(input(f"{red}Give side b:{white} "))
            c = float(input(f"{red}Give hypotenuse c:{white} "))
            a = round(math.sqrt(c ** 2 - b ** 2), 1)
            print(f"{red}The length of the side a is:{yellow} {a}")
        elif side == "b":
            a = float(input(f"{red}Give side a:{white} "))
            c = float(input(f"{red}Give hypotenuse c:{white} "))
            b = round(math.sqrt(c ** 2 - a ** 2), 1)
            print(f"{red}The length of the side b is:{yellow} {b}")
        elif side == "c":
            a = float(input(f"{red}Give side a:{white} "))
            b = float(input(f"{red}Give side b:{white} "))
            c = round(math.sqrt(a ** 2 + b ** 2), 1)
            print(f"{red}The length of the hypotenuse c is:{yellow} {c}")
        else:
            print(f"{red}Invalid input")
    except ValueError:
        print(f"{red}Please enter numbers only.")
    input()
    os.system("cls")  # Clear terminal
def currency_converter():
    Ask_for_Amount = True
    def converter(amount, from_currency, to_currency):
        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    def print_currency_list():
        print(f"{red}Choose from the following currencies:")
        print("1. USD - US Dollar")
        print("2. EUR - Euro")
        print("3. JPY - Japanese Yen")
        print("4. GBP - British Pound Sterling")
        print("5. AUD - Australian Dollar")
        print("6. CAD - Canadian Dollar")
        print("7. CHF - Swiss Franc")
        print("8. CNY - Chinese Yuan Renminbi")
        print("9. SEK - Swedish Krona")
        print("10. NZD - New Zealand Dollar")
        print("11. INR - Indian Rupee")
        print("12. ZAR - South African Rand")
        print("13. AED - UAE Dirham")
        print("14. BRL - Brazilian Real")
        print("15. SGD - Singapore Dollar")
        print("16. MXN - Mexican Peso")
        print("17. NOK - Norwegian Krone")
        print("18. TRY - Turkish Lira")
        print("19. KRW - South Korean Won")
        print("20. CZK - Czech Crown")
    print_currency_list()
    while Ask_for_Amount:
        try:
            amount = float(input(f"{red}Enter the amount:{white} "))
            from_currency = input(f"{red}Enter the code of the source currency:{white} ").upper()
            to_currency = input(f"{red}Enter the code of the target currency:{white} ").upper()
            converted_amount = converter(amount, from_currency, to_currency)
            print(f"{yellow}{amount} {from_currency}{red} is equal to {yellow}{converted_amount:.2f} {to_currency}")
            Ask_for_Amount = False
            input()
        except ValueError:
            print(f"{red}Please enter valid number and currency codes.")
def steganography():
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
    main()
    input()
    os.system("cls")  # Clear terminal
def wifispeedtest():
    test = speedtest.Speedtest(secure=True)
    def bytes_to_mb(bytes):
        KB = 1024  # One Kilobyte is 1024 bytes
        MB = KB * 1024  # One MB is 1024 KB
        return int(bytes / MB)
    print(f"{red}Wifi speed test")
    download_speed = bytes_to_mb(test.download())
    print(f"{red}Your Download speed is{yellow}", download_speed, "MB")
    upload_speed = bytes_to_mb(test.upload())
    print(f"{red}Your Upload speed is{yellow}", upload_speed, "MB")
    input()
    os.system("cls")  # Clear terminal
def zip_generate():
    file = fd.askopenfilename()
    if path.exists(file):
        print("Select file in the folder you want to archive")
        src = path.realpath(file)
        root_dir, tail = path.split(src)
        name = input("Name for the archived folder: ") + " Archive"
        shutil.make_archive(name, "zip", root_dir)
        input()
        os.system("cls")  # Clear terminal
    else:
        print("File doesn't exist")
def yt_download():
    def download_video(url):
        try:
            subprocess.run(["youtube-dl", url])
            print("Video Downloaded successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    url = input("Enter YouTube Video URL: ")
    download_video(url)
def language_detection():
    text = input(f"{red}Enter any text in any language:{white} ")
    print(red + detect(text))
    input()
    os.system("cls")  # Clear terminal
def Enc_Dec():
    Run_else_if_wrong_number = True
    Run_select_what_cipher = True
    while Run_select_what_cipher == True:
        choice = input(f"{bred}[{yellow}1{bred}]{red}  Caesar cipher\n{bred}[{yellow}2{bred}]{red}  Atbash cipher\n{bred}[{yellow}3{bred}]{red}  Vigenère Cipher\n:{white} ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{red}Please select a number")
            input()
            os.system("cls")
            Run_else_if_wrong_number = False
        if choice == 1:
            Run_select_what_cipher = False
            ceasar_cipher()
        elif choice == 2:
            Run_select_what_cipher = False
            atbash_cipher()
        elif choice == 3:
            Run_select_what_cipher = False
            vigenere_cipher()
        else:
            if Run_else_if_wrong_number == True:
                print(f"{red}Invalid selection press enter to try again")
                input()
                os.system("cls")
            else:
                continue
def ceasar_cipher():
    Ask_all_question = True
    while Ask_all_question:
        def ceasar_encrypt(text, key):
            result = ""
            for char in text:
                if char.isalpha():
                    shift = 65 if char.isupper() else 97
                    result += chr((ord(char) - shift + key) % 26 + shift)
                else:
                    result += char
            return result
        def caesar_decrypt(cipher_text, key):
            return ceasar_encrypt(cipher_text, -key)
        os.system("cls")
        print(f"{red}This Encryption does not work with numbers and special characters!")
        choice = input(f"{red}Encrypt or Decrypt? (e/d):{white} ").lower()
        if choice == "e":
            Ask_all_question = False
            text = input(f"{red}Enter the text:{white} ")
            key = int(input(f"{red}Enter the key (a number between 1 and 25):{white} "))
            encrypted_text = ceasar_encrypt(text, key)
            print(f"{red}Encryption\n{yellow}{text} -> {encrypted_text}\nKey:{key}")
        elif choice == "d":
            Ask_all_question = False
            text = input(f"{red}Enter the text:{white} ")
            key = int(input(f"{red}Enter the key (a number between 1 and 25):{white} "))
            decrypted_text = caesar_decrypt(text, key)
            print(f"{red}Decryption\n{yellow}{text} -> {decrypted_text}")
        elif choice != "d" or "e":
            print(f"{red}Please use 'e' or 'd'")
        input()
        os.system("cls")  # Clear terminal
def atbash_cipher():
    Ask_all_question = True
    while Ask_all_question:
        def atbash_cipher(text):
            result = ""
            for char in text:
                if char.isalpha():
                    shift = 65 if char.isupper() else 97
                    result += chr((25 - (ord(char) - shift)) + shift)
                else:
                    result += char
            return result
        def atbash_decipher(text):
            return atbash_cipher(text)
        os.system("cls")
        print(f"{red}This Encryption does not work with numbers and special characters!")
        choice = input(f"{red}Encrypt or Decrypt? (e/d):{white} ").lower()
        if choice == "e":
            Ask_all_question = False
            text = input(f"{red}Enter the text:{white} ")
            encrypted_text = atbash_cipher(text)
            print(f"{red}Encryption\n{yellow}{text} -> {encrypted_text}")
        elif choice == "d":
            Ask_all_question = False
            text = input(f"{red}Enter the text:{white} ")
            decrypted_text = atbash_decipher(text)
            print(f"{red}Decryption\n{yellow}{text} -> {decrypted_text}")
        elif choice != "d" or "e":
            print(f"{red}Please use 'e' or 'd'")
        input()
        os.system("cls")  # Clear terminal
def vigenere_cipher():
    Ask_all_questions = True
    while Ask_all_questions:
        def vigenere_cipher(plain_text, key):
            result = ''
            key_len = len(key)
            for i, char in enumerate(plain_text):
                if char.isalpha():
                    shift = 65 if char.isupper() else 97
                    key_char = key[i % key_len]
                    key_shift = ord(key_char) - 65 if key_char.isupper() else ord(key_char) - 97
                    result += chr(((ord(char) - shift + key_shift) % 26) + shift)
                else:
                    result += char
            return result
        def vigenere_decrypt(ciphertext, key):
            result = ""
            key_len = len(key)
            for i, char in enumerate(ciphertext):
                if char.isalpha():
                    shift = 65 if char.isupper() else 97
                    key_char = key[i % key_len]
                    key_shift = ord(key_char) - 65 if key_char.isupper() else ord(key_char) - 97
                    result += chr(((ord(char) - shift - key_shift) % 26) + shift)
                else:
                    result += char
            return result
        print(f"{red}This Encryption does not work with numbers and special characters!")
        choice = input(f"{red}Encrypt or Decrypt? (e/d):{white} ").lower()
        if choice == "e":
            Ask_all_questions = False
            text = input(f"{red}Enter the text:{white} ")
            key = input(f"{red}Enter the key (a word):{white} ")
            encrypted_text = vigenere_cipher(text, key)
            print(f"{red}Encryption\n{yellow}{text} -> {encrypted_text}\nKey:{key}")
        elif choice == "d":
            Ask_all_questions = False
            text = input(f"{red}Enter the text:{white} ")
            key = input(f"{red}Enter the key (a word):{white} ")
            decrypted_text = vigenere_decrypt(text, key)
            print(f"{red}Encryption\n{yellow}{text} -> {decrypted_text}\nKey:{key}")
        elif choice != "d" or "e":
            print(f"{red}Please use 'e' or 'd'")
        input()
        os.system("cls")  # Clear terminal
def password_strength(password):
    criteria = [
        (r'.{8,}', 2),       # Minimum length of 8 characters
        (r'[a-z]', 1),        # Lowercase letters
        (r'[A-Z]', 2),        # Uppercase letters
        (r"\d", 1),           # Digits
        (r'[@#$%^&+=]', 2)
    ]
    score = 0
    for pattern, weight in criteria:
        if re.search(pattern, password):
            score += weight
    return score
def main():
    try:
        while True:
            os.system("cls")
            print(f"""
{cyan}   ___  _ _ _____           _     _____      _____            
{blue}  / _ \| | |_   _|         | |   |_   _|    |  _  |           
{cyan} / /_\ \ | | | | ___   ___ | |___  | | _ __ | | | |_ __   ___ 
{blue} |  _  | | | | |/ _ \ / _ \| / __| | || '_ \| | | | '_ \ / _ \ 
{cyan} | | | | | | | | (_) | (_) | \__ \_| || | | \ \_/ / | | |  __/
{blue} \_| |_/_|_| \_/\___/ \___/|_|___/\___/_| |_|\___/|_| |_|\___|
{yellow}{" " * 58}[{cyan}v1{yellow}]
{cyan}{" "*48}[{blue}By {green}\x56\x6f\x6a\x74\x61\x76\x6c\x61\x73{cyan}]                                                                                                            
""")
            try:
                print(Options)
                tool = int(input(f"{bred}AllToolsInOne:{white} "))
                if tool == 1:
                    os.system("cls")
                    print(f"{red}File needs to be png to work")
                    input()
                    file = fd.askopenfilename()
                    bg_removal(file)
                elif tool == 2:
                    os.system("cls")
                    print(f'{red}Type an address you want to shorten:{white} ')
                    url_shortener(input(""))
                elif tool == 3:
                    os.system("cls")
                    Run_code = True
                    while Run_code:
                        print(f"{bred}[{yellow}1{bred}]{red} Url\n{bred}[{yellow}2{bred}]{red} Wifi\n{bred}[{yellow}3{bred}]{red} Text")
                        try:
                            choice_for_qr_code = int(input(": "))
                        except ValueError:
                            print(f"{red}You need to type a number, not a string")
                            input()
                            Run_code = False
                        if Run_code == True:
                            Run_code = False
                            if choice_for_qr_code == 1:
                                url = str(input(f"{red}Url for qr code:{white} "))
                                qrcodegenerator_url(url)
                            elif choice_for_qr_code == 2:
                                qrcodegenerator_wifi()
                            elif choice_for_qr_code == 3:
                                text = str(input(f"{red}Type a text you want to convert to qr code:{white} "))
                                qrcodegenerator_text(text)
                            else:
                                Run_code = True
                elif tool == 4:
                    os.system("cls")
                    file = fd.askopenfilename()
                    mp4_to_mp3(file)
                elif tool == 5:
                    os.system("cls")
                    PasswordGenerator()
                elif tool == 6:
                    os.system("cls")
                    Pythagoras_theorem_solver()
                elif tool == 7:
                    os.system("cls")
                    currency_converter()
                elif tool == 8:
                    os.system("cls")
                    steganography()
                elif tool == 9:
                    os.system("cls")
                    wifispeedtest()
                elif tool == 10:
                    os.system("cls")
                    zip_generate()
                elif tool == 11:
                    os.system("cls")
                    yt_download()
                elif tool == 12:
                    os.system("cls")
                    language_detection()
                elif tool == 13:
                    os.system("cls")
                    Enc_Dec()
                elif tool == 14:
                    os.system("cls")
                    password = input(f"{bred}Enter a password:{white} ")
                    strength = password_strength(password)
                    if strength <= 3:
                        print(f"{red}Password is weak")
                    elif strength <= 6:
                        print(f"{yellow}Password is moderate")
                    else:
                        print(f"{green}Password is strong")
                    input()
                elif tool == 15:
                    os.system("cls")
                    hash_input = str(input(f"{bred}Type the hash you want to identify:{white} "))
                    command = f"hashid {hash_input}"
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    output_lines = [line for line in result.stdout.split('\n') if line.startswith('[+]')]
                    print(f"{green}All the possible hashes")
                    print('\n'.join(output_lines))
                    input()
                elif tool == 16:
                    os.system("cls")
                elif tool == 17:
                    os.system("cls")
                elif tool == 18:
                    os.system("cls")
                elif tool == 19:
                    os.system("cls")
                elif tool == 20:
                    os.system("cls")
                elif tool == 21:
                    shortened_url = input(f"{red}Url u want to unshorten:{white}")
                    if not shortened_url.startswith("http"):
                        shortened_url = "https://" + shortened_url
                    try:
                        response = requests.head(shortened_url, allow_redirects=True)
                        unshortened_url = response.url
                        print(f"{red}The unshortened URL is: {unshortened_url}")
                        input()
                    except requests.exceptions.RequestException as e:
                        print(f"{red}Failed to unshorten URL: {e}")
                        input()
                    os.system("cls")
                elif tool == 00 or 0:
                    print(f"{red} Exiting...")
                    time.sleep(1)
                    os.system("cls")
                    break
                else:
                    print(f"{red}Invalid choice. Please choose a valid option.")
                    input()
            except ValueError:
                print(f"{red}Please enter a number.")
                input()
                os.system("cls")
    except KeyboardInterrupt:
        print(f"{red}\nExiting...")
        time.sleep(1)
        os.system("cls")
if __name__ == "__main__":
    main()   