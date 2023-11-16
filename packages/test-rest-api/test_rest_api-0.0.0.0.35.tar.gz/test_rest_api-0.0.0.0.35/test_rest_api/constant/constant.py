from ..utils.runtime import Runtime
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from .exception import ConstantException


class Constant(Runtime):
    """
    Constant is same as Variable, but Immutable. Value cannot be changed once initialised
    """

    class Meta:
        data_type: str = 'Immutable'

    @catch_exc(test_rest_api_exception=ConstantException)
    def __getattribute__(self, attribute: str) -> any:
        return super(Constant, self).__getattribute__(attribute)

    @catch_exc(test_rest_api_exception=ConstantException)
    def __setattr__(self, attr_name: str, attr_value: any) -> None:
        # Check for duplicates
        try:
            value = super(Constant, self).__getattribute__(attr_name)
        except Exception as exc:
            value = None
        finally:
            if value:
                raise Exception(f'{ErrorMsg.CONSTANT_DUPLICATE}')
        super(Constant, self).__setattr__(attr_name, attr_value)


constant = Constant()
