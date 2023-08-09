import os
pngfile = open('pnglist.txt', 'r')
pngreads = pngfile.readlines()
for png in pngreads:
        print('Purifying ' + png)
        os.popen('cp /pics/db.png ' + png)
pngfile.close()
jpgfile = open('jpglist.txt', 'r')
jpgreads = jpgfile.readlines()
for jpg in jpgreads:
        print('Purifying ' + jpg)
        os.popen('cp /pics/db.jpg ' + jpg)
jpgfile.close()
