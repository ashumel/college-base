'''
Описать класс согласно индивидуальному варианту. В классе должно быть как минимум 2 поля,
конструктор, метод для вывода на экран всей информации об объекте, метод уничтожающий объект. В
основной программе создать объект при помощи конструктора, вывести на экран информацию, которую в
объект заносит ваш конструктор, затем поменять значения полей объекта и еще раз вывести всю
информацию об объекте на экран.
Класс Фотоаппарат. (Примерные поля: фирма, зум, число мегапикселей матрицы)
'''

class camera:
    def __init__(self, vendor, zoom, camera_mp):
        self.vendor = vendor
        self.zoom = zoom
        self.camera_mp = camera_mp
    def returnInformation(self):
        print(self.vendor)
        print(self.zoom)
        print(self.camera_mp)
    def __del__(self):
        print('Класс очищен')


user_camera = camera('Canon', 105, 20.1)
user_camera.returnInformation()
user_camera.vendor = '1234567890'
user_camera.returnInformation()