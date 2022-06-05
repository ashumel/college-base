from PIL import Image, ImageDraw, ImageFont
# Пустой желтый фон.
im = Image.new('RGB', (1000, 600), (219, 193, 27))
draw = ImageDraw.Draw(im)

# Рисуем красный эллипс с черной оконтовкой.
draw.ellipse((150, 100, 220, 200), fill='red', outline=(0, 0, 0))

# Рисуем синий квадрат с белой оконтовкой.
draw.rectangle((200, 110, 300, 200), fill='blue', outline=(255, 255, 255))

# Рисуем прямоугольник
draw.rectangle((400, 400, 300, 200), fill='green', outline=(255, 255, 255))

# Рисуем Окружность.
draw.ellipse((390, 100, 600, 300), fill='yellow', outline=(0, 0, 0))

# Рисуем розовую линию с шириной в 10 пиксель.
draw.line((300, 200, 450, 100), fill='pink', width=10)

#Рисуем многоугольник (в нашем случаи триугольник)
draw.polygon(
    xy=(
 (200, 400),
 (340, 200),
 (300, 300)
 ), fill='brown', outline=(0, 0, 0)
)

#Рисуем Дугу
draw.arc(
 xy=(25, 50, 150, 200),
 start=30, end=270,
 fill='red'
)

#Рисуем хорду
draw.chord(
 xy=(350, 50, 400, 100),
 start=30, end=270, fill=(255, 255, 0),
 outline=(0, 0, 0)
)

#Теперь надо сделать кусок пирога
draw.pieslice(
 xy=(500, 100, 575, 200),
 start=30, end=270, fill=(255, 255, 0),
 outline=(0, 0, 0)
)

#Рисуем текст

font = ImageFont.truetype('ipo_labs/lab18/Gilroy-Medium.ttf', size=18)
draw_text = ImageDraw.Draw(im)
draw_text.text( 
 (100, 30),
 'Привет, меня зовут Даниил, мне 17 лет',
 # Добавляем шрифт к изображению
 font=font,
 fill='#1C0606')

#Вставка изображения
watermark = Image.open('ipo_labs/lab18/watermark.png')
im.paste(watermark, (50,450), watermark)

im.show()