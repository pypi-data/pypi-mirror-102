import requests
from requests.compat import urljoin, quote_plus

from data_grid_surface.config.config import BASE_URL
from data_grid_surface.services.hash import sha256


class DataGrid:

    def __init__(self, **kwargs):
        if not kwargs:
            raise Exception("Missing credentials config dictionary!")
        if 'username' not in kwargs:
            raise Exception("Missing username in config dictionary!") 
        if 'password' not in kwargs:
            raise Exception("Missing password in config dictionary!") 

        self.base_url = BASE_URL
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.token = ''


    def __api_call(self, method, url, data={}, token=''):
        """Send an API request

        Arguments:
        method -- HTTP method to be used
        url -- URL to API end-point 

        Keyword arguments:
        data -- parameters to be sent with an API requrest (default {})
        """

        headers = {}
        if token:
            headers['x-access-token'] = token

        try:
            if method == 'GET':
                response = requests.get(url, params=data, headers=headers)
            elif method == 'POST':
                response = requests.post(url, data=data, headers=headers)
            
            return response.json()

        except requests.exceptions.ConnectionError:
            return { "Error": "Couldn't connect with API server!" }
        except Exception as e:
            return { "Error": "Some error occured during API call!" }


    def __validate_token(self):
        url = urljoin(self.base_url, quote_plus('auth/verifytoken', safe='/'))
        response = self.__api_call('POST', url, { "token": self.token })
        if response.get('status', False) == 'fail':
            return self.__set_token()
        return response


    def __set_token(self):
        url = urljoin(self.base_url, quote_plus('auth/signin', safe='/'))
        response = self.__api_call('POST', url, { "username": self.username, "password": self.password })
        if response['status'] == 'fail':
            return response
        self.token = response['data']['accessToken']
        return response


    def check_email(self, email, is_hashed=True):
        """Send API request to check if email exists in database

        Arguments:
        email -- email to be checked

        Default arguments:
        is_hashed -- flag which determines if email is raw or hashed (default True)
        """
        
        try:
            response = self.__validate_token()
            if response.get('status', False) == 'fail':
                return response

            if not is_hashed:
                email = sha256(email.lower())
            
            url = urljoin(self.base_url, f'emails/{quote_plus(email)}')
            return self.__api_call('GET', url, token=self.token)

        except Exception as e:
            return e


    def check_password(self, password, is_hashed=True):
        """Send API request to check if password exists in database

        Arguments:
        password -- password to be checked

        Default arguments:
        is_hashed -- flag which determines if password is raw or hashed (default True)
        """

        try:
            response = self.__validate_token()
            if response.get('status', False) == 'fail':
                return response

            if not is_hashed:
                password = sha256(password)

            url = urljoin(self.base_url, f'passwords/{quote_plus(password)}')
            return self.__api_call('GET', url, token=self.token)
        
        except Exception as e:
            return e

        
    def check_phone_number(self, phone_number, is_hashed=True):
        """Send API request to check if phone number exists in database

        Arguments:
        phone_number -- phone number to be checked

        Default arguments:
        is_hashed -- flag which determines if password is raw or hashed (default True)
        """

        try:
            response = self.__validate_token()
            if response.get('status', False) == 'fail':
                return response

            if not is_hashed:
                phone_number = sha256(phone_number)

            url = urljoin(self.base_url, f'phone-numbers/{quote_plus(phone_number)}')
            print(url)
            return self.__api_call('GET', url, token=self.token)
        
        except Exception as e:
            return e