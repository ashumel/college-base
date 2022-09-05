afile = open(r'ipo_labs/lab10_t2/user_str.txt', 'w')
user_str = ''
while user_str != ' ':
    user_str = input('Введите строку:')
    afile.write(user_str + '\n')