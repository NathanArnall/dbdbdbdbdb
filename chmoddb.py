import os
pngfile = open('pnglist.txt', 'r')
pngreads = pngfile.readlines()
for png in pngreads:
        print('Purifying ' + png)
        os.popen('chmod +w ' + png)
        os.popen('cp ~/dbedition/db.png ' + png)
pngfile.close()
jpgfile = open('jpglist.txt', 'r')
jpgreads = jpgfile.readlines()
for jpg in jpgreads:
        print('Purifying ' + jpg)
        os.popen('chmod +w ' + jpg)
        os.popen('cp ~/dbedition/db.jpg ' + jpg)
jpgfile.close()
svgfile = open('svglist.txt', 'r')
svgreads = svgfile.readlines()
for svg in svgreads:
        print('Purifying ' + svg)
        os.popen('chmod +w ' + svg)
        os.popen('cp ~/dbedition/db.svg ' + svg)
svgfile.close()
print('Purification complete')
