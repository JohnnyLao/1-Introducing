import requests

# Task 1

def get_the_smartest_hero(base_url):
    int_dict = {}
    hulk_url, captain_america_url, thanos_url = base_url + "/powerstats/332.json", \
                                                base_url + "/powerstats/149.json", \
                                                base_url + "/powerstats/655.json"
    hulk_resp, captain_america_resp, thanos_resp = requests.get(hulk_url), \
                                                   requests.get(captain_america_url), \
                                                   requests.get(thanos_url)
    hulk_dict, captain_america_dict, thanos_dict = hulk_resp.json(), \
                                                   captain_america_resp.json(), \
                                                   thanos_resp.json()
    int_dict['Hulk'], int_dict['Captain America'], int_dict["Thanos"] = captain_america_dict['intelligence'], \
                                                                        thanos_dict['intelligence'], \
                                                                        hulk_dict['intelligence']
    the_smartest_hero = max(int_dict, key=int_dict.get)
    print(f'Самый умный супергерой - {the_smartest_hero}')


# Task 2

import os

TOKEN = ''


class Yaloader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {token}'}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get('href', '')
        result = requests.put(href, data=open(path_to_file, 'rb'))
        if result.status_code == 201:
            print('Загрузка завершена')
        else:
            print(f'Ошибка загрузки! Код ошибки: {result.status_code}')


if __name__ == '__main__':
    # Task 1
    get_the_smartest_hero("https://akabab.github.io/superhero-api/api")
    # Task 2
    path_to_file = os.path.join(os.getcwd(), 'text.txt')
    print(path_to_file)
    token = TOKEN
    uploader = Yaloader(token)
    result = uploader.upload('text.txt')
