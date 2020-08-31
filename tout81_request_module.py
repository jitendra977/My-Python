def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import json
    import requests

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=c66ee65c7e324fd59e2551b305ddbbd8')
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    response = requests.get(url)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])
    print(response.json())
