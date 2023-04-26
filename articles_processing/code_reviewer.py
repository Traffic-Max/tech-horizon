import requests
import json

API_KEY = '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'  # Замените на свой API-ключ
API_URL = 'https://api.openai.com/v1/models/code-davinci-edit-001/completions'


HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def review_code(code, max_tokens=2048):
    prompt = f'Проверьте и исправьте код, если это необходимо:\n{code}\n---\n'
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
        reviewed_code = response_data['choices'][0]['text']
        return reviewed_code.strip()
    else:
        print(f'Ошибка API: {response.status_code}')
        return None

def main():
    code_to_review = '''
Введи код для проверки.
    '''

    reviewed_code = code_to_review
    num_checks = 3

    for i in range(num_checks):
        print(f'Цикл проверки {i + 1}:\n')
        reviewed_code = review_code(reviewed_code)
        if reviewed_code:
            print(f'Проверенный и исправленный код:\n{reviewed_code}\n')
        else:
            print('Ошибка во время проверки кода.')
            break

if __name__ == '__main__':
    main()




"""
#xhatgpt 3.5 turbo
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "Hello!"}]
}



"""
