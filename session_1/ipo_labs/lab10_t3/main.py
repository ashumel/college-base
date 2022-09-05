import codecs
afile = codecs.open(r'ipo_labs/lab10_t3/fish_text.txt', 'r', 'utf_8')
count = 0
for line in afile:
    count = count + 1
    word_list = line.split()
    print(len(line), len(word_list))
print(count)