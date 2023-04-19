##### 
##### Author: Hai-Anh Le
##### Date  : May 28, 2015
#####
import json

## read json file
fileName = input("BAGEL file name: ")
with open("./" + fileName, 'r') as f:
    inFile = json.load(f)
coordinates = []
natom = 0
fulljson = inFile['bagel']
geomjson = fulljson[0]['geometry']
natom = len(geomjson)
for i in range(natom):
  atom = geomjson[i]['atom']
  x = str(geomjson[i]['xyz'][0])
  y = str(geomjson[i]['xyz'][1])
  z = str(geomjson[i]['xyz'][2])
  coordinates.append(atom + "    " + x + "    " + y + "    " + z)

## write xyz file
stem = fileName.split(".")
outFile = open(stem[0] + ".xyz", 'w')
outFile.write(str(natom) + "\n")
outFile.write(fileName + " in xyz format\n")
for point in coordinates:
  outFile.write(point + "\n")

outFile.close()

