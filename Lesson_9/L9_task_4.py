import re
f = open(r'd:\\Python_ITed\\Lesson_9\\L9_task_4.txt','r')
text = f.read()
arr = text.split()
d = {}
for i in arr:
   s = len((re.findall(i, text)))
   d.update({i: s})
f.close()
print(d)