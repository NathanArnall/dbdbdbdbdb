import os
pngfile = open('pnglist.txt', 'r')
pngreads = pngfile.readlines()
for png in pngreads:
        print('Purifying ' + png)
        os.popen('cp ~/dbedition/db.png ' + png)
pngfile.close()
jpgfile = open('jpglist.txt', 'r')
jpgreads = jpgfile.readlines()
for jpg in jpgreads:
        print('Purifying ' + jpg)
        os.popen('cp ~/dbedition/db.jpg ' + jpg)
jpgfile.close()
