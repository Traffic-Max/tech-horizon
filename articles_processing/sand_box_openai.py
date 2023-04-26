import os
from PIL import Image
import openai

# Устанавливаем ключ API OpenAI
openai.api_key = "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"

MAX_SIZE = 4 * 1024 * 1024  # 4 МБ
filename = ""

# Проверяем размер файла и формат
if os.path.getsize(filename) > MAX_SIZE:
    # Изменяем имя файла
    filename = f"{filename[:-4]}_resized.png"

    # Открываем изображение и изменяем его размер
    image = Image.open(filename)
    size = (int(image.size[0] / 2), int(image.size[1] / 2))  # Уменьшаем размер вдвое
    image = image.resize(size)

    # Сохраняем изображение
    image.save(filename)

    print("Размер файла изображения был уменьшен до 4 МБ.")
elif not filename.lower().endswith(".png"):
    print("Ошибка: файл должен быть в формате PNG.")
else:
    print("Файл изображения соответствует требованиям.")

# Создаем варианты изображения с помощью OpenAI API
with open(filename, "rb") as f:
    response = openai.Image.create_variation(
        image=f,
        n=2,
        size="1024x1024"
    )

    print(response)
