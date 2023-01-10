import json
import requests


def call_chatgpt_api(quest):
    auth_token = "COLE_AQUI_SUA_API_KEY"
    header = {
        "Authorization": "Bearer " + auth_token
    }
    data = {
        "model": "text-davinci-003",
        "prompt": quest,
        "temperature": 1,
        "max_tokens": 500
    }

    # API
    url = "https://api.openai.com/v1/completions"
    resp = requests.post(url, json=data, headers=header)
    return resp.text


def process_response(elements):
    return json.loads(elements)['choices'][0]['text'].strip()


if __name__ == '__main__':
    question = "Qual a raíz quadrada de 144?"
    print(process_response(call_chatgpt_api(question)))
