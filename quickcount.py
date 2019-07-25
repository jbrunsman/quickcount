
#
#  Counts the number of files in each directory down from current working directory
#

import os

fileCount = []

print('Quick Count\n')

for root, dirs, files in os.walk("."):
    if len(files) > 0:
        thisCount = [root, str(len(files))]
        fileCount.append(thisCount)
        #print(root + '   ' + str(len(files)))

for row in fileCount:
    print("{:.<60}{:.>6}".format(*row))

input('\nPress any key to exit...')
