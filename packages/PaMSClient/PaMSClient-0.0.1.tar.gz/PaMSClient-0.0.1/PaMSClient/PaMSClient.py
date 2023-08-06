import threading
import requests


class PaMSClient(object):
    def __init__(
            self,
            url: str,
            token: str
    ):
        self.__url = url
        self.__token = token

        self.__cache = self.__call_api()
        self.__auto_refresh = ''
        self.__is_auto_refresh = False

    def __set_interval(self, seconds):
        def function_wrapper():
            self.__set_interval(seconds)
            self.refresh_cache()

        self.__auto_refresh = threading.Timer(seconds, function_wrapper)
        self.__auto_refresh.start()

    def __call_api(self):
        r = requests.get(self.__url + '?token=' + self.__token, allow_redirects=True)

        if r.status_code != 200:
            return print(f'The API server respond with an http error code: {r.status_code}.')
        elif r.json() == {'error_code': 'pams_wrong_token'}:
            return print('Token authentication failed.')

        return r.json()

    def __use_cache(self):
        return self.__call_api() if self.__cache == '' else self.__cache

    def get_cache(self):
        return self.__cache

    def clear_cache(self):
        self.__cache = ''

    def refresh_cache(self):
        self.__cache = self.__call_api()

    def set_auto_refresh_cache(self, ms):
        self.__set_interval(ms / 1000)
        self.__is_auto_refresh = True

    def stop_auto_refresh_cache(self):
        if self.__is_auto_refresh:
            self.__auto_refresh.cancel()
            self.__is_auto_refresh = False
        else:
            return print('Auto refresh not active.')

    def get_last_check(self):
        return self.__use_cache()['infos']['requestid']

    def get_global_status(self):
        return self.__use_cache()['infos']['global_status']

    def get_request_id(self):
        return self.__use_cache()['infos']['lastcheck']

    def get_service_by_ID(
            self,
            service_id: str
    ):
        r = self.__use_cache()
        return_value = ''

        for x in r['categories']:
            for x2 in r['categories'][x]['services']:
                if x2 == service_id:
                    return_value = r['categories'][x]['services'][x2]

                    for x3 in return_value:
                        if return_value[x3] == '[none]':
                            return_value[x3] = None

        return return_value if return_value != '' else None

    def get_service_by_cat(
            self,
            cat_name: str,
            service_id: str
    ):
        r = self.__use_cache()
        return_value = ''

        for x in r['categories'][cat_name]['services']:
            if x == service_id:
                return_value = r['categories'][cat_name]['services'][x]

                for x2 in return_value:
                    if return_value[x2] == '[none]':
                        return_value[x2] = None

        return return_value if return_value != '' else None

    def get_service_by_name(
            self,
            service_name: str
    ):
        r = self.__use_cache()
        return_value = ''

        for x in r['categories']:
            for x2 in r['categories'][x]['services']:
                for x3 in r['categories'][x]['services'][x2]:
                    if r['categories'][x]['services'][x2][x3] == service_name:
                        return_value = r['categories'][x]['services'][x2]

        return return_value if return_value != '' else None

    def get_all_services(self):
        r = self.__use_cache()
        services_list = []

        for x in r['categories']:
            for x2 in r['categories'][x]['services']:
                services_list.append(x2)
        return services_list
