import os

def StringToHex():
    os.system("clear")
    x = raw_input("Convert String to Hex (word/string): ")
    print x.encode("hex")

def HexToString():
    os.system("clear")
    x = raw_input("Convert Hex to String (hex code): ")
    print x.decode("hex")
