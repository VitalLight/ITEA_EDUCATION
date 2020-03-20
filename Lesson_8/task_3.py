
file1 = open('d:\\Python_ITed\\test python.txt','r')
f1 = file1.readlines()
file2 = open('d:\\Python_ITed\\test python2.txt','r')
f2 = file2.readlines()
file3 = open('d:\\Python_ITed\\test python 3.txt','w')
file3.writelines(f1)
file3.writelines(f2)
file3.close()
