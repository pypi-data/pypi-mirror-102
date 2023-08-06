import requests


class ConsultService:
    __URL = "http://www.consultant.ru/law/ref/calendar/proizvodstvennye/"
    __IS_PROXY = False

    def __init__(self, proxy):
        if proxy:
            self.__IS_PROXY = True

            if not (proxy['login'] or proxy['password'] or proxy['url']):
                raise ValueError("Empty config proxy data")
            else:
                self.__proxy = f"http://{proxy['login']}:{proxy['password']}@{proxy['url']}"

    # Returns html content
    def get_html_content(self, year):
        if self.__IS_PROXY:
            response = requests.get(url=f"{self.__URL}{year}/", proxies={"http": self.__proxy})
        else:
            response = requests.get(url=f"{self.__URL}{year}/")

        if response.status_code == requests.codes.ok:
            return response.text
        else:
            raise requests.HTTPError

    # Checks for content availability
    def is_content_available(self, year):
        if self.__IS_PROXY:
            response = requests.get(url=f"{self.__URL}{year}/", proxies={"http": self.__proxy})
        else:
            response = requests.get(url=f"{self.__URL}{year}/")

        if response.status_code == requests.codes.ok:
            return True

        return False
