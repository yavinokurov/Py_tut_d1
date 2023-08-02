import requests

host = "https://wttr.in/"
places = ['London', 'svo', 'Череповец']

def print_weather(location):
    payload = {'M': '', 'nTqu': '', 'lang': 'ru'}
    response = requests.get(''.join((host, location)), params=payload)
    print(response.text)


if __name__ == "__main__":
    for place in places:
        print_weather(place)
