from PIL import Image as img
from PIL import ImageFilter as img_filter

try:
    image = img.open('ipo_labs/lab17/darkholme.jpg')
    image_5 = img.open('ipo_labs/lab17/darkholme.jpg')
    print(f'Исходное изображение: {image.format, image.size, image.mode}')


    image_1 = image.rotate(30).save('ipo_labs/lab17/image_1.jpg')
    image_2 = image.crop((400, 400, 800, 800)).save('ipo_labs/lab17/image_2.jpg')
    print(f'Изображение 3: {image.format, image.size, image.mode}')
    image_3 = image.resize((int(image.size[0] / 2), int(image.size[1] / 2))).save('image_3.jpg')
    print(f'Изображение 4: {image.format, image.size, image.mode}')
    image_4 = image.transpose(img.FLIP_LEFT_RIGHT).save('ipo_labs/lab17/image_4.jpg')
    image_5.thumbnail((128, 128))
    image_5.save('image_5.jpg')
    image_6 = image.filter(img_filter.CONTOUR).save('ipo_labs/lab17/image_6.jpg')
    print(f'Изображение 6: {image.format, image.size, image.mode}')
    image_7 = image.filter(img_filter.DETAIL).save('ipo_labs/lab17/image_7.jpg')
    image_8 = image.filter(img_filter.EDGE_ENHANCE).save('ipo_labs/lab17/image_8.jpg')

except FileNotFoundError:
    print('Файл не был обнаружен')