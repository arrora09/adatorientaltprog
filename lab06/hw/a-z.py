import sys
import os

script_name = os.path.basename(sys.argv[0])

print(script_name)

alphabet = "abcdefghijklmnopqrstuvwxyz"

if script_name == "z-a.py":
    print(alphabet[::-1])
else:
    print(alphabet)
