import requests
import json
import yaml
from datetime import date
import random

API_KEY = 'your_api_key'  # Замените на свой API-ключ
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_yaml_block(markdown_content):
    lines = markdown_content.split('\n')
    yaml_lines = []

    inside_yaml_block = False
    for line in lines:
        if line.strip() == '---':
            inside_yaml_block = not inside_yaml_block
        elif inside_yaml_block:
            yaml_lines.append(line)

    return '\n'.join(yaml_lines)

def generate_text(prompt, max_tokens=50):
    data = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'n': 1,
        'stop': None,
        'temperature': 0.7,
    }

    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data['choices'][0]['text'].strip()
    else:
        print(f'Ошибка API: {response.status_code}')
        return None

def translate_text(text, source_language, target_language, max_tokens=2048):
    prompt = f'Переведите следующий текст с {source_language} на {target_language}: {text}'
    data = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'n': 1,
        'stop': None,
        'temperature': 0.7,
    }

    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        response_data = json.loads(response.text)
        translated_text = response_data['choices'][0]['text']
        return translated_text.strip()
    else:
        print(f'Ошибка API: {response.status_code}')
        return None

def process_yaml(yaml_content, text):
    metadata = yaml.safe_load(yaml_content)

    # Установка текущей даты без времени
    metadata['date'] = date.today().isoformat()

    # Добавление описания с помощью ИИ, если оно отсутствует
    if not metadata.get('description'):
        description_prompt = f"Напишите краткое описание для статьи на тему: {metadata['title']}"
        metadata['description'] = generate_text(description_prompt, max_tokens=50)

    # Проверка релевантности хештегов и внесение корректировок с помощью ИИ
    tags_prompt = f"Предложите 5 релевантных хештегов для статьи на тему: {metadata['title']}"
    suggested_tags = generate_tags(tags_prompt)  # Убираем передачу model и tokenizer
    new_tags = list(set(metadata['tags'] + suggested_tags))
    metadata['tags'] = random.sample(new_tags, min(len(new_tags), 5))

    return metadata


def extract_text(markdown_content):
    # Извлечение текста статьи из Markdown содержимого
    lines = markdown_content.split('\n')
    text_lines = [line for line in lines if line.strip() != '---']
    return '\n'.join(text_lines)


def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def extract_yaml_block(markdown_content):
    lines = markdown_content.split('\n')
    yaml_lines = []
    for line in lines:
        if line.strip() == '---':
            break
        yaml_lines.append(line)
    return '\n'.join(yaml_lines)


def split_text(text, max_length=2048):
    words = text.split(' ')
    groups = []
    current_group = []

    for word in words:
        if len(' '.join(current_group) + ' ' + word) <= max_length:
            current_group.append(word)
        else:
            groups.append(current_group)
            current_group = [word]

    if current_group:
        groups.append(current_group)

    return groups


def main():
    file_path = 'your_markdown_file.md'  # Замените на путь к файлу Markdown
    markdown_content = read_markdown_file(file_path)
    yaml_content = extract_yaml_block(markdown_content)
    metadata = process_yaml(yaml_content, text)
    text = extract_text(markdown_content)

    # Обработка текста статьи и перевода
    source_language = 'английского'
    target_language = 'русский'
    text_groups = split_text(text)
    translated_text = ''

    for group in text_groups:
        group_text = '\n'.join(group)
        if translated_group := translate_text(
            group_text, source_language, target_language
        ):
            translated_text += translated_group + '\n'
        else:
            print('Ошибка во время перевода текста.')

    print(f'Перевод:\n{translated_text}')

    # Проверка релевантности перевода с помощью ключевых слов
    keywords_prompt = f"Предложите 5 ключевых слов для статьи на тему: {metadata['title']}"
    suggested_keywords = generate_tags(keywords_prompt, model, tokenizer)
    for keyword in suggested_keywords:
        if keyword.lower() not in translated_text.lower():
            print(f'Возможно, перевод не полностью релевантен, так как ключевое слово "{keyword}" отсутствует в переведенном тексте.')


if __name__ == '__main__':
    main()
