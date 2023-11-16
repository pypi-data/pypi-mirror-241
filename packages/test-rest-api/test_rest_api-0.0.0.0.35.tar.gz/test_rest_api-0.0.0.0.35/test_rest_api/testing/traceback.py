import re


class FormatTraceback:
    def __init__(self):
        self.header = '\nTRACEBACKS\n----------\n'
        self.re_search_start = r'test_rest_api[//\\]testing[//\\]decorator.py", line (.*?), in inner\n    await func\(\*args, \*\*kwargs\)\n'

    def test_rest_api_exc(self, traceback: str) -> str:
        re_search_end = r'raise test_rest_api_exception'
        start_res = re.search(self.re_search_start, traceback)
        end_res = re.search(re_search_end, traceback)
        traceback = traceback[start_res.end():end_res.end()]
        traceback = traceback[:traceback.rfind('File "') - 3]
        return f'{self.header}{traceback}'

    def bug_exc(self, traceback: str) -> str:
        re_search_end = r'raise Bug'
        start_res = re.search(self.re_search_start, traceback)
        end_res = re.search(re_search_end, traceback)
        traceback = traceback[start_res.end():end_res.end()]
        return f'{self.header}{traceback}'

    def rest_api_creation_exc(self, traceback: str) -> str:
        re_search_end = r'raise RestApiCreationException'
        start_res = re.search(self.re_search_start, traceback)
        end_res = re.search(re_search_end, traceback)
        traceback = traceback[start_res.end():end_res.end()]
        traceback = traceback[:traceback.rfind('File "') - 3]
        if re.search(r'test_rest_api[//\\]rest_api[//\\]rest_api.py", line (.*?), in __call__', traceback):
            traceback = traceback[:traceback.rfind('File "') - 3]
            traceback = traceback[:traceback.rfind('File "') - 3]
        return f'{self.header}{traceback}'

    def assert_exc(self, traceback: str) -> str:
        re_search_end = r'raise AssertException'
        start_res = re.search(self.re_search_start, traceback)
        end_res = re.search(re_search_end, traceback)
        traceback = traceback[start_res.end():end_res.end()]
        traceback = traceback[:traceback.rfind('File "') - 3]
        return f'{self.header}{traceback}'

    def assert_error(self, traceback: str) -> str:
        re_search_end = r'\nAssertionError'
        start_res = re.search(self.re_search_start, traceback)
        traceback = traceback[start_res.end():]
        end_res = re.search(re_search_end, traceback)
        traceback = traceback[:end_res.start()]
        if 'assert False, exc.args[0]' in traceback:
            traceback = traceback[:traceback.rfind('File "') - 3]
        return f'{self.header}{traceback}'

    def unexpected_exc(self, traceback: str) -> str:
        start_res = re.search(self.re_search_start, traceback)
        traceback = traceback[start_res.end():]
        return f'{self.header}{traceback}'


format_traceback = FormatTraceback()
