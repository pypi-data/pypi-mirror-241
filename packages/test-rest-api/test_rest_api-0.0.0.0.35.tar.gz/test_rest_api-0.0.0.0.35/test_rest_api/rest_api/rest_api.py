from dataclasses import asdict
from aiohttp.client_exceptions import ClientConnectorError, InvalidURL, ContentTypeError
from .. import settings
from .method import RestApiMethod
from ..utils.error_msg import ErrorMsg
from ..utils.aiohttp_session import AioHttpSession
from .response import RestApiResponse, ClientResponse
from ..utils.exception import catch_exc, catch_exc_async
from .exception import RestApiSendException, RestApiCreationException


class RestApi:
    """
    Class for creating rest api instances
    """
    # Create a frozen instance of RestApiMethod, so that it can be used as a constant in code
    METHODS = RestApiMethod()

    def _validate(self):
        """
        Validate url, parameters, headers and body
        """
        self._validate_url()
        self._validate_parameters_and_headers()
        self._validate_body()

    def _validate_url(self):
        """
        Checks
        ------
        1. Valid string
        """
        if not isinstance(self.url, str):
            raise Exception('Invalid data type for url. Please provide a valid string')

    def _validate_parameters_and_headers(self):
        """
        Checks
        ------
        1. Valid dictionary
        2. Valid dictionary schema
        """
        error = 'Please provide a valid dictionary, with both dictionary key and dictionary value as string type'
        for item in ('parameters', 'headers'):
            if not isinstance(getattr(self, item), dict):
                raise Exception(f'Invalid data type for {item}. {error}')
            if not all([isinstance(key, str) and isinstance(key, str) for key, value in
                        getattr(self, item).items()]):
                raise Exception(f'Invalid dictionary for {item}. {error}')

    def _validate_body(self):
        """
        Checks
        ------
        1. Valid dictionary
        """
        if not isinstance(self.body, dict):
            raise Exception('Invalid data type for body. Please provide a valid dictionary')

    @catch_exc(test_rest_api_exception=RestApiCreationException)
    def __init__(self, url: str, parameters: dict = {}, headers: dict = {}, body: dict = {}):
        # Rest api variables
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self.body = body
        # Validate url, parameters, headers and body
        self._validate()
        # Aiohttp session
        self._session = AioHttpSession()
        # Logging
        print(f'\nRest Api Created\n----------------{self}')

    def __str__(self):
        return f"""
 {settings.logging.sub_point} Url         {settings.logging.key_val_sep} {self.url}
 {settings.logging.sub_point} Headers     {settings.logging.key_val_sep} {self.headers}
 {settings.logging.sub_point} Parameters  {settings.logging.key_val_sep} {self.parameters}
 {settings.logging.sub_point} Body        {settings.logging.key_val_sep} {self.body}
"""

    async def _create_response(self, response: ClientResponse) -> RestApiResponse:
        """
        Create response instance object from aiohttp async response
        """
        # Retrieve the response body in JSON
        # Only supports application/json content type
        body = await response.json() if response.content_type == 'application/json' else {}
        # Get the other response parameters
        status_code, headers, content_type = response.status, dict(response.headers), response.content_type
        # Create and return the RestApiResponse instance object
        rest_api_response = RestApiResponse(status_code=status_code,
                                            content_type=content_type,
                                            body=body,
                                            headers=headers,
                                            obj=response)
        # Logging
        print(f'Rest Api Response\n-----------------{rest_api_response} ')
        return rest_api_response

    async def _send(self, method: str):
        """
        Send the rest api by providing the request method
        """
        try:
            # Logging
            print(
                f'Rest Api Send\n-------------\n {settings.logging.sub_point} Method      {settings.logging.key_val_sep} {method.upper()}\n')
            # Check if method is of type string
            if not isinstance(method, str):
                raise Exception('Invalid data type for method. Please provide a valid string')
            # Convert to lowercase
            method = method.lower()
            # Check if the method is valid
            if method not in asdict(self.METHODS).values():
                raise Exception(ErrorMsg.INVALID_METHOD)
            # Send the request
            async with getattr(self._session, method)(url=self.url,
                                                      params=self.parameters,
                                                      headers=self.headers,
                                                      json=self.body) as response:
                return await self._create_response(response=response)
        except ClientConnectorError:
            raise Exception(ErrorMsg.CLIENT_CONNECTOR_ERROR)
        except InvalidURL:
            raise Exception(ErrorMsg.INVALID_URL)
        except ContentTypeError:
            raise Exception(ErrorMsg.INVALID_JSON_RESPONSE)
        except Exception as exc:
            raise exc

    @catch_exc_async(test_rest_api_exception=RestApiSendException)
    async def send(self, method: str):
        """
        Send the rest api by providing the request method
        """
        return await self._send(method=method)

    @catch_exc_async(test_rest_api_exception=RestApiSendException)
    async def get(self):
        """
        Send HTTP GET Request
        """
        return await self._send(method=self.METHODS.GET)

    async def post(self):
        """
        Send HTTP POST Request
        """
        return await self._send(method=self.METHODS.POST)

    async def put(self):
        """
        Send HTTP PUT Request
        """
        return await self._send(method=self.METHODS.PUT)

    async def patch(self):
        """
        Send HTTP PATCH Request
        """
        return await self._send(method=self.METHODS.PATCH)

    async def delete(self):
        """
        Send HTTP DELETE Request
        """
        return await self._send(method=self.METHODS.DELETE)

    async def head(self):
        """
        Send HTTP HEAD Request
        """
        return await self._send(method=self.METHODS.HEAD)

    async def options(self):
        """
        Send HTTP OPTIONS Request
        """
        return await self._send(method=self.METHODS.OPTIONS)
