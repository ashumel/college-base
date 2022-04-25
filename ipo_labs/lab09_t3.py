days_month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 30, 6 : 30, 7 : 31, 8 : 29, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

def date_ver2(day, month, year):
    try:
        if day <= days_month.get(month) and year > 0:
            return True
        else: return False
    except:
        return False


day = int(input())
month = int(input())
year = int(input()) #* Заглушка :)

print(date_ver2(day, month, year))