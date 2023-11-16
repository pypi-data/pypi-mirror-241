from inspect import getframeinfo, stack
from .. import settings
from ..testing.bug import Bug
from .exception import AssertException
from ..utils.decorator_hints import decorated_func_param_hints


@decorated_func_param_hints
def catch_exc(func):
    """
    Catch the exceptions and raise new exception
    AssertionError exception will be re raised using the bug obj passed
    Rest all errors will be raised as AssertException to make the test status as ERROR
    NOTE: We are using a custom catch_exc, because we need raise assert with bug params which will be dynamic value
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError as exc:
            assert False, exc.args[0]
        except Exception as exc:
            raise AssertException(msg=str(exc))

    return inner


class Assert:
    """
    Custom Assert Class for performing assertions
    Advantages of using this over python inbuilt assert statement -> Rich reporting for both pass and fail scenarios
    """

    @staticmethod
    def _log(*, code, assertion):
        print(f"""
Assertion
---------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {code}
 {settings.logging.sub_point} Assert {settings.logging.key_val_sep} {assertion}
""")

    @staticmethod
    def _assert(*, assertion, bug):
        # Logging
        Assert._log(code=getframeinfo(stack()[4][0]).code_context[0].strip(), assertion=assertion)
        # Perform the assertion using python inbuilt assert statement
        exec(f'{assertion}, bug')

    @staticmethod
    def _format_args(func):
        def inner(*args, **kwargs):
            """
            This is done to avoid error caused by strings, in exec() function
            """
            args = [f"'{arg}'" if isinstance(arg, str) else arg for arg in args]
            kwargs = {key: f"'{value}'" if isinstance(value, str) else value for key, value in kwargs.items()}
            func(*args, **kwargs)

        return inner

    @staticmethod
    @catch_exc
    @_format_args
    def equal(arg1, arg2, bug=Bug()):
        """
        Check if arg1 == arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} == {arg2}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def not_equal(arg1, arg2, bug=Bug()):
        """
        Check if arg1 != arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} != {arg2}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def true(arg, bug=Bug()):
        """
        Check if arg == True
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def false(arg, bug=Bug()):
        """
        Check if arg == False
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert not {arg}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def greater(arg1, arg2, bug=Bug()):
        """
        Check if arg1 > arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} > {arg2}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def lesser(arg1, arg2, bug=Bug()):
        """
        Check if arg1 < arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} < {arg2}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def greater_equal(arg1, arg2, bug=Bug()):
        """
        Check if arg1 >= arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} >= {arg2}', bug=bug)

    @staticmethod
    @catch_exc
    @_format_args
    def lesser_equal(arg1, arg2, bug=Bug()):
        """
        Check if arg1 <= arg2
        Raise your custom Bug if needed
        """
        Assert._assert(assertion=f'assert {arg1} <= {arg2}', bug=bug)
