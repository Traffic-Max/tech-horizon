from PIL import Image



# Открыть JPEG-изображение
jpeg_image = Image.open("articles_processing/1.jpeg")

# Сохранить его в формате PNG
# jpeg_image.save("1.png")

# Закрыть файл
# jpeg_image.close()



# Открыть изображение
# image = Image.open("1.lpeg")

# Изменить размер до квадрата
size = (min(jpeg_image.size), min(jpeg_image.size))
image = jpeg_image.resize(size)

# Сохранить изображение
image.save("2.png")
