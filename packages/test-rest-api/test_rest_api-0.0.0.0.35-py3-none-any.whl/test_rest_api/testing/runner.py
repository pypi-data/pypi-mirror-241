import os
import sys
import json
import types
import aiohttp
import asyncio
import traceback
import importlib.machinery
from datetime import datetime
from time import perf_counter_ns
from inspect import getmembers, iscoroutinefunction
from . import utils
from . import decorator
from ..reporting.report import Report
from ..utils.error_msg import ErrorMsg
from ..utils.string_color import str_color
from ..test_data.test_data import testdata
from ..utils.logger import test_rest_api_logger
from ..environment.environment import environment
from ..utils.aiohttp_session import AioHttpSession


class BaseRunnerMeta(type):
    def __new__(cls, name, bases, attrs):
        """Fetch and store validate_ methods for Auto validation"""
        if not getattr(cls, '_validation_method_names', None):
            cls._validation_method_names = []
        for method_name in [attr for attr in attrs if attr.startswith("validate_")]:
            if method_name not in cls._validation_method_names:
                cls._validation_method_names.append(method_name)
        attrs['_validation_method_names'] = cls._validation_method_names
        return super(BaseRunnerMeta, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        """Perform validations"""
        obj = super(BaseRunnerMeta, cls).__call__(*args, **kwargs)
        for method_name in obj._validation_method_names:
            if (method_obj := getattr(obj, method_name, None)):
                method_obj()
        return obj


class BaseRunner(metaclass=BaseRunnerMeta):
    def __init__(self, test_suite_path, test_result_path=None, env_path=None, test_data_path=None, test_tags=[]):
        # Initialise instance variables
        self.test_suite_path = test_suite_path
        self.env_path = env_path
        self.test_data_path = test_data_path
        # Test result path is optional and by default its test suite path
        self.test_result_path = test_result_path if test_result_path else test_suite_path
        # Test tags is optional and by default it's an empty list
        self.test_tags = test_tags.split("#") if test_tags and test_tags.startswith('#') else []
        # Remove empty tags
        self.test_tags = [test_tag for test_tag in self.test_tags if test_tag]

    def validate_test_suite_path(self):
        """Validate test suite path"""
        conditions = (self.test_suite_path, os.path.exists(self.test_suite_path))
        if all(conditions):
            return
        sys.exit(ErrorMsg.INVALID_TEST_SUITE_PATH)

    def validate_test_result_path(self):
        """Validate test result path"""
        if os.path.exists(self.test_result_path):
            return
        sys.exit(ErrorMsg.INVALID_TEST_RESULT_PATH)

    def validate_test_env_path(self):
        """Validate test Env path"""
        # Env path is optional
        if not self.env_path:
            return
        if os.path.exists(self.env_path):
            return
        sys.exit(ErrorMsg.INVALID_ENV_PATH)

    def validate_test_tags(self):
        """Validate test tags"""
        # Test data path is optional
        if not self.test_data_path:
            return
        if os.path.exists(self.test_data_path):
            return
        sys.exit(ErrorMsg.INVALID_TEST_TAG)

    def validate_test_data_path(self):
        """Validate test data path"""
        # Test data path is optional
        if not self.test_data_path:
            return
        if os.path.exists(self.test_data_path):
            return
        sys.exit(ErrorMsg.INVALID_TEST_DATA_PATH)

    @staticmethod
    def console_branding():
        """
        Package branding in Console
        """
        test_rest_api_logger.info(str_color.brand(f'''
                              =======================================================
                            || ..................................................... ||
                            || ..................................................... ||
                            || ...........  T E S T - R E S T - A P I   ............ ||
                            || ..................................................... ||
                            || ..................................................... ||
                              =======================================================
                            '''))

    @staticmethod
    def console_sync_test_title():
        """
        Sync Tests Title in Console
        """
        test_rest_api_logger.info(str_color.brand(f'''
                          =======================================================
                        || ................  S Y N C - T E S T S ............... ||
                          ======================================================='''))

    @staticmethod
    def console_async_test_title():
        """
        Async Tests Title in Console
        """
        test_rest_api_logger.info(str_color.brand(f'''
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          ======================================================='''))

    @staticmethod
    def console_summary(report: Report):
        """
        Test Summary in Console
        """
        test_rest_api_logger.info(str_color.brand('''
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          ======================================================='''))
        try:
            # TODO : change the way of printing , for each new value i need to come here and change
            test_rest_api_logger.info(str_color.info(f'''
                         {'Status:' : <20}{'PASS' if report.summary.test.status else 'FAIL'}
                         {'Tests:' : <20}{report.summary.tests.total}
                         {'Start:' : <20}{report.summary.test.start}
                         {'End:' : <20}{report.summary.test.end}
                         {'Duration:' : <20}{report.summary.test.duration}
                         {'Tags:' : <20}{report.summary.test.tags}

                         {'PASS:' : <20}{report.summary.tests.success}
                         {'FAIL:' : <20}{report.summary.tests.fail}
                         {'ERROR:' : <20}{report.summary.tests.error}
                         {'DISABLE:' : <20}{report.summary.tests.disable}
                         {'SKIP:' : <20}{report.summary.tests.skip}

                         {'LOW:' : <20}{report.summary.bugs.low}
                         {'MINOR:' : <20}{report.summary.bugs.minor}
                         {'MAJOR:' : <20}{report.summary.bugs.major}
                         {'CRITICAL:' : <20}{report.summary.bugs.critical}
                         {'BLOCKER:' : <20}{report.summary.bugs.blocker}

                         {'REST API:' : <20}{report.summary.errors.rest_api}
                         {'ENVIRONMENT:' : <20}{report.summary.errors.environment}
                         {'TEST DATA:' : <20}{report.summary.errors.test_data}
                         {'VARIABLE:' : <20}{report.summary.errors.variable}
                         {'CONSTANT:' : <20}{report.summary.errors.constant}
                         {'BUG:' : <20}{report.summary.errors.bug}
                         {'ASSERTION:' : <20}{report.summary.errors.assertion}
                         {'UNEXPECTED:' : <20}{report.summary.errors.unexpected}'''))
        except Exception as exc:
            test_rest_api_logger.info(str_color.info(f'''
                         Invalid Report Object
                         Error: {exc}'''))

    @staticmethod
    def load_module(name: str, path: str):
        """
        Load the module in runtime and return it
        """
        loader = importlib.machinery.SourceFileLoader(name, path)
        module = types.ModuleType(name)
        loader.exec_module(module)
        return module

    @staticmethod
    def load_sync_tests(module):
        """
        From test file load all the @test decorated sync function objects in a list
        Conditions: Is sync Function & Decorated with @test
        """
        return [obj for _, obj in getmembers(module) if
                iscoroutinefunction(obj) and obj.__dict__.get('is_testcase', False) and not obj.__dict__.get(
                    'is_async_testcase', False)]

    @staticmethod
    def load_async_tests(module):
        """
        From test file load all the @test decorated async function objects in a list
        Conditions: Is Async Function & Decorated with @test
        """
        return [obj for _, obj in getmembers(module) if
                iscoroutinefunction(obj) and obj.__dict__.get('is_testcase', False) and obj.__dict__.get(
                    'is_async_testcase', False)]


class Runner(BaseRunner):
    """
    Execute all test cases
    Auto detect test suites and test cases
    """

    def __init__(self, test_suite_path, test_result_path=None, env_path=None, test_data_path=None, test_tags=[]):
        # Initialise Base Class
        super(Runner, self).__init__(test_suite_path, test_result_path, env_path, test_data_path, test_tags)
        # List of test file paths
        self.test_files: list = []
        # List of test data file paths
        self.test_data_files: list = []
        # List of @test decorated sync function objects
        self.sync_tests: list = []
        # List of @test decorated async function objects
        self.async_tests: list = []
        #
        utils.test_tags = self.test_tags
        #
        self.report = Report()
        decorator.report = self.report

    def load_tests(self):
        """
        Auto-detect @test decorated sync and async functions from the list of test python files
        Update the function objects in tests list
        """
        # Create a generator of python files from testsuite folder
        test_file_generator = (test_file for test_file in self.test_files)
        # For each file path in list of python files from testsuite folder
        for test_file in test_file_generator:
            # Get file name with extension
            name_with_ext = os.path.basename(self.test_suite_path)
            # Get file name without extension
            name = os.path.splitext(name_with_ext)[0]
            # Load the module in runtime from file paths
            module = Runner.load_module(name=name, path=test_file)
            # Load the @test decorated sync functions as a list from the module
            sync_tests = Runner.load_sync_tests(module)
            # Update the sync_tests instance variable
            self.sync_tests.extend(sync_tests)
            # Load the @test decorated async functions as a list from the module
            async_tests = Runner.load_async_tests(module)
            # Update the async_tests instance variable
            self.async_tests.extend(async_tests)

    def load_test_files(self, path):
        """
        Auto-detect python files from a test suite folder/file path to a list
        Files can be under any nested folder
        """
        if path.endswith("__pycache__") or path.endswith(".json"):
            return
        if os.path.isfile(path) and path.endswith('.py'):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + "/" + nested_path)

    def setup_testsuite(self):
        """
        Run before test suite execution
        - Load the python files from the input path provided
        - Load all the @test decorated functions from the list of python files
        - Add env data to global variables as constants
        """
        # Logging
        test_rest_api_logger.info(str_color.info('Starting test setup'))
        # Logging
        test_rest_api_logger.info(str_color.info('Auto detecting test suites'))
        # Load python files
        self.load_test_files(self.test_suite_path)
        # Logging
        test_rest_api_logger.info(str_color.info(f'Total test suites: {len(self.test_files)}'))
        test_rest_api_logger.info(str_color.info('Auto detecting tests'))
        # Load @test decorated functions from the loaded python files
        self.load_tests()
        # Logging
        test_rest_api_logger.info(str_color.info(f'Total synchronous tests: {len(self.sync_tests)}'))
        test_rest_api_logger.info(str_color.info(f'Total asynchronous tests: {len(self.async_tests)}'))
        test_rest_api_logger.info(str_color.info(f'Total tests: {len(self.sync_tests) + len(self.async_tests)}'))
        # Sen environment
        environment._set(path=self.env_path)
        # Set test data
        testdata._set(path=self.test_data_path)

    async def run_testsuite(self):
        """
        Run the test suite
        """
        # Package Branding in console
        Runner.console_branding()
        # Set up the testsuite before run
        self.setup_testsuite()
        # Exit if the total testcases = 0
        if len(self.sync_tests) + len(self.async_tests) == 0:
            sys.exit(ErrorMsg.EMPTY_TESTS)
        # Logging
        test_rest_api_logger.info(str_color.info('Started sorting the synchronous tests'))
        # Sort the synchronous tests
        self.sync_tests.sort(key=lambda x: x.execution_order)
        # Session should be created inside async function even if it itself not an async function
        # Also creation should happen inside the main event loop (Should not be in a separate event loop)
        session = aiohttp.ClientSession(json_serialize=json.dumps)
        # Create an aiohttp session for the whole run instead of creating a new session per request.
        AioHttpSession.set(session=session)
        # Logging
        test_rest_api_logger.info(str_color.info('Created aiohttp client session'))
        test_rest_api_logger.info(str_color.info('Completed test setup'))
        if len(self.sync_tests) > 0:
            Runner.console_sync_test_title()
        # Start the stopwatch / counter
        timer_start = perf_counter_ns()
        # Test start date time
        start = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # Create a generator of synchronous tests
        sync_test_generator = (sync_test for sync_test in self.sync_tests)
        # Run synchronous tests before async tests
        for sync_test in sync_test_generator:
            await sync_test()
        # Logging
        if len(self.async_tests) > 0:
            Runner.console_async_test_title()
        # Running Tasks Concurrently (Execute async functions concurrently)
        await asyncio.gather(*[async_test() for async_test in self.async_tests], return_exceptions=False)
        # Test end time
        end = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # Stop the stopwatch / counter
        timer_stop = perf_counter_ns()
        # Calculate the time duration of the test in seconds (note: duration is in nanoseconds)
        duration = f'{(timer_stop - timer_start) / 1000000000} seconds'
        # Update report summary details
        self.report.summary.test.start = start
        self.report.summary.test.end = end
        self.report.summary.test.duration = duration
        self.report.summary.test.tags = self.test_tags
        # Close the aiohttp session after completing the test
        await AioHttpSession().close()
        # Create the test report
        self.report.save(path=self.test_result_path)
        # Summary result in console
        Runner.console_summary(report=self.report)

    def run(self):
        """
        Method to run the testsuite
        This method can be used by the users to trigger the test in code.
        example:
                from test_rest_api import Runner
                runner = Runner(test_suite_path="<Test Suite Path>")
                runner.run()
        """
        try:
            # Run 'run_testsuite' coroutine in an event loop.
            asyncio.run(self.run_testsuite())
        except Exception as exc:
            sys.exit(f"""
{ErrorMsg.UNKNOWN_EXCEPTION}
Error details: {exc}
{traceback.format_exc()}
""")
