import os
import lib

h = (["hex","Hex","H","h","HEX"])
s = (["str","Str","STR","s","S","String","string","STRING"])

ask = raw_input("Convert to (hex/string): ")

if ask in (h):
   lib.StringToHex()

if ask in (s):
   lib.HexToString()
