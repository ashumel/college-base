msg = str('Привет, Андрей, ну где ты был, ну обними меня скорей!')

def string_center(string):
    return string[(len(string)-1)//2:(len(string)+8)//2]

print(msg[:8])
print(string_center(msg))
print(msg[-5:])