import os
import sys
from dotenv import dotenv_values
from ..utils.runtime import Runtime
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from ..utils.string_color import str_color
from .exception import EnvironmentException
from ..utils.logger import test_rest_api_logger


class Environment(Runtime):
    """
    Environment can be used for parameterization in rest api creation
    """

    class Meta:
        data_type: str = 'Immutable'

    @catch_exc(test_rest_api_exception=EnvironmentException)
    def __getattribute__(self, attribute: str) -> any:
        return super(Environment, self).__getattribute__(attribute)

    @catch_exc(test_rest_api_exception=EnvironmentException)
    def __setattr__(self, attr_name: str, attr_value: any):
        raise Exception(ErrorMsg.ENVIRONMENT_RUNTIME_SET)

    def _set(self, *, path: str) -> None:
        """
        Set environment from file path. Supported file extensions: env
        """
        # Set environment from .env file
        self._set_from_env_file(path=path)

    def _set_from_env_file(self, *, path: str) -> None:
        """
        Set environment variables from .env file
        """
        # Return if path is empty or None
        if not path:
            return
        # Logging
        test_rest_api_logger.info(str_color.info(f'Configuring environment from .env file'))
        try:
            # Get env file
            env = dotenv_values(path)
            # Create constant global variables
            for name, value in env.items():
                # Set environment
                self._set_attr(attr_name=name, attr_value=value)
        except Exception as exc:
            sys.exit(str_color.exception(f'{exc}\nFile : {os.path.basename(path)}\nPath : {path}'))
        # Logging
        test_rest_api_logger.info(str_color.info(f'Initialised {len(env)} environment values from .env file'))

    def _set_attr(self, *, attr_name: str, attr_value: any) -> None:
        """
        Set the class attribute
        """
        # String representation of attr_name & attr_value for exception messages
        input_details = f'\nName : {attr_name}\nValue: {attr_value}'
        # Check if name is of type string
        if not isinstance(attr_name, str):
            raise Exception(f'{ErrorMsg.ENVIRONMENT_INVALID_DATA_TYPE}{input_details}')
        # Check if name not empty
        if attr_name.strip() == '':
            raise Exception(f'{ErrorMsg.ENVIRONMENT_EMPTY_STRING}{input_details}')
        # Check for duplicates
        try:
            value = super(Environment, self).__getattribute__(attr_name)
        except Exception as exc:
            value = None
        finally:
            if value:
                raise Exception(f'{ErrorMsg.ENVIRONMENT_DUPLICATE}{input_details}')
        # Set class level attribute
        # Call the base version of __setattr__ you avoid the infinite recursive error
        super(Environment, self).__setattr__(attr_name, attr_value)


environment = Environment()
