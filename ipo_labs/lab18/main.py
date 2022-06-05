from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (1000, 600), (72, 72, 72))
draw = ImageDraw.Draw(im)
draw.ellipse((50, 50, 200, 200), 'yellow', outline = (255, 255, 255))
draw.ellipse((200, 150, 300, 200), 'yellow', outline = (255, 255, 255))
draw.rectangle((350, 150, 400, 200), fill = 'blue', outline=(255, 255, 255))
draw.rectangle((450, 150, 600, 200), fill = 'blue', outline=(255, 255, 255))
draw.line(xy=((650, 150),(800, 100)), fill = 'red', width=10)
draw.polygon(xy=((850, 200),(900, 400),(400, 400)), fill = 'blue', outline=(255, 255, 255))
draw.arc(xy=(50, 50, 400, 400), start=30, end=270 ,fill = 'red')
draw.chord(xy=(225, 50, 375, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
draw.pieslice(xy=(425, 50, 575, 200),start=30, end=270, fill=(255, 255, 0),outline=(0, 0, 0))
draw.text((200,200),'Я учусь на слесаря-инструментальщика',fill=('white'),
          font= ImageFont.truetype('ipo_labs/lab18/Gilroy-Medium.ttf', size=18))
watermark = Image.open('ipo_labs/lab18/watermark.png')
im.paste(watermark, (10,450), watermark)
im.show()