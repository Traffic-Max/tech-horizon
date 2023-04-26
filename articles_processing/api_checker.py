import requests
import json

API_KEY = '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'  # Замените на свой API-ключ
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def check_api_key_and_url(api_key, api_url):
    data = {
        "prompt": "Test",
        "max_tokens": 5,
        "num_return_sequences": 1,
        "stop": None,
        "temperature": 1.0,
        "top_p": 1.0,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
        "num_beams": 1,
        "echo": False,
    }

    response = requests.post(url=api_url, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        print("API-ключ и URL-адрес API корректны.")
        return True
    else:
        print(f"Ошибка: API-ключ или URL-адрес API некорректны. Код ошибки: {response.status_code}")
        return False

if __name__ == '__main__':
    check_api_key_and_url(api_key=API_KEY, api_url=API_URL)


"""
Модели, в названии которых есть «код», являются частью «Кодекса» — они служат для генерации кода.

Модели, в названии которых есть «текст», служат для создания обычного текста (это их основная цель, но они также могут генерировать код в небольшой степени).

Модели, в названии которых есть «поиск» или «сходство», предназначены для «встраивания» — они служат для поиска похожих текстов (как описано в документации в разделе «вложения»).

Модели, имеющие в названии «search-code», предназначены для поиска по «коду», «search-text» — для поиска по тексту. Модели, у которых в названии есть «поиск», но нет «кода», предназначены для поиска по тексту («документ» — для указания документов, среди которых вы ищете, «запрос» — для запроса, по которому вы ищете). «Сходство» также используется для поиска похожих документов, но есть некоторая разница между «поиском» и «сходством». Насколько я помню, в основном речь идет о длине искомых документов.

Модели с «редактировать» предназначены для редактирования кода или текста (в отличие от его завершения).

Модели с «инструкцией» — это модели, обученные специально для обработки ввода (подсказки) в форме или инструкциях.

Модели с «insert» предназначены для вставок (вы передаете [insert] в подсказке, и она генерирует текст/код в середине подсказки, вместо того, чтобы генерировать «insert» в конце).

«001», «002» — разные версии. Я предполагаю, что «002» лучше, чем «001», потому что 002 — это улучшенная версия 001.

Я не знаю, что такое модели с «если».

{
      "id": "code-search-ada-code-001",
      "object": "model",
      "created": 1651172507,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-8soch45iiGvux5Fg1ORjdC4s",
          "object": "model_permission",
          "created": 1669087421,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "code-search-ada-code-001",
      "parent": null
    },
{
      "id": "ada-code-search-text",
      "object": "model",
      "created": 1651172510,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-kFc17wOI4d1FjZEaCqnk4Frg",
          "object": "model_permission",
          "created": 1669087421,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "ada-code-search-text",
      "parent": null
    },
{
      "id": "code-search-ada-text-001",
      "object": "model",
      "created": 1651172507,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-JBssaJSmbgvJfTkX71y71k2J",
          "object": "model_permission",
          "created": 1669087421,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "code-search-ada-text-001",
      "parent": null
    },

{
      "id": "ada-code-search-code",
      "object": "model",
      "created": 1651172505,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-wa8tg4Pi9QQNaWdjMTM8dkkx",
          "object": "model_permission",
          "created": 1669087421,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "ada-code-search-code",
      "parent": null
    },
 {
      "id": "code-search-babbage-code-001",
      "object": "model",
      "created": 1651172507,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-64LWHdlANgak2rHzc3K5Stt0",
          "object": "model_permission",
          "created": 1669085864,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "code-search-babbage-code-001",
      "parent": null
    },
{
      "id": "code-search-babbage-text-001",
      "object": "model",
      "created": 1651172507,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-EC5ASz4NLChtEV1Cwkmrwm57",
          "object": "model_permission",
          "created": 1669085863,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "code-search-babbage-text-001",
      "parent": null
    },
{
      "id": "babbage-code-search-text",
      "object": "model",
      "created": 1651172509,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-Lftf8H4ZPDxNxVs0hHPJBUoe",
          "object": "model_permission",
          "created": 1669085863,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "babbage-code-search-text",
      "parent": null
    },
{
      "id": "code-davinci-edit-001",
      "object": "model",
      "created": 1649880484,
      "owned_by": "openai",
      "permission": [
        {
          "id": "modelperm-Foe5Y4TvaKveYxt74oKMw8IB",
          "object": "model_permission",
          "created": 1679934178,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": false,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "code-davinci-edit-001",
      "parent": null
    },
{
      "id": "babbage-code-search-code",
      "object": "model",
      "created": 1651172509,
      "owned_by": "openai-dev",
      "permission": [
        {
          "id": "modelperm-4qRnA3Hj8HIJbgo0cGbcmErn",
          "object": "model_permission",
          "created": 1669085863,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ],
      "root": "babbage-code-search-code",
      "parent": null
    },

я отобрал все модели со словом code, выбери наиболее подходящую для нашиз целей, ты же помнишь наши цели? 

"""