import requests

host = "https://wttr.in/"


def print_weather(location):
    payload = {'lang': 'ru'}
    x = requests.get(''.join((host, location, '?M', 'nTqu')), params=payload)
    print(x.text)
    return True


print_weather('London')
print_weather('svo')
print_weather('Череповец')
