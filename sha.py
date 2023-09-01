# Python program to find SHA256 hexadecimal hash string of a file
import hashlib
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]

for filename in onlyfiles:
    if (".deb" in filename):
        with open(filename,"rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest()
            print(filename + "(" + str(len(bytes)) + "): " + readable_hash)