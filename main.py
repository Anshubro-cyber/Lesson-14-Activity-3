file1 = open('a.txt','r')

file2 = open('au.txt','w')

for line in file1.readlines():

    if not (line.startswith('The')):

        print(line)

        file2.write(line)
file2.close()
file1.close()