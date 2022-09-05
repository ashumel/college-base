
import codecs
afile = codecs.open(r'ipo_labs/lab10_t1/students.txt', 'r', 'utf_8')

lines = afile.readlines()
marksCount = 0
marksNumber = 0
for line in lines:
    marksCount = marksCount + 1
    if int(line.strip()[-1:]) <= 3:
        print(line.strip()[:-1])
    marksNumber = marksNumber + int(line.strip()[-1:])

print(marksNumber / marksCount)