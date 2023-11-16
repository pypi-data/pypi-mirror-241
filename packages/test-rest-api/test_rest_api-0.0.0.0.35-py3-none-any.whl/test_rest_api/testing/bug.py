from dataclasses import dataclass, asdict
from .. import settings
from ..utils.exception import catch_exc
from .exception import BugCreationException


@dataclass(frozen=True)
class BugPriority:
    """
    Supported bug priority values
    """
    LOW: str = 'low'
    MINOR: str = 'minor'
    MAJOR: str = 'major'
    CRITICAL: str = 'critical'
    BLOCKER: str = 'blocker'


class Bug(Exception):
    """
    Terminate the current test by raising Bug exception inside test async function
    """

    PRIORITY = BugPriority()

    def _validate(self):
        """
        Checks
        ------
        1. All attributes are string datatype
        2. Valid supported bug priority value
        """
        self._validate_datatype()
        self._validate_priority()

    def _validate_datatype(self):
        """
        Checks
        ------
        1. message is a valid string
        2. priority is a valid string
        3. actual_result is a valid string
        4. expected_result is a valid string
        5. steps_to_reproduce is a valid string
        """
        for item in ('message', 'priority', 'actual_result', 'expected_result', 'steps_to_reproduce'):
            if not isinstance(getattr(self, item), str):
                raise Exception(f'Invalid data type for {item}. Please provide a valid string')

    def _validate_priority(self):
        """
        Checks
        ------
        1. Valid bug priority
        """
        bug_priority_list = asdict(BugPriority()).values()
        # Check if the priority value is valid
        if self.priority.lower() not in bug_priority_list:
            raise Exception(f'Invalid bug priority value\nSupported bug priorities: {", ".join(bug_priority_list)}')

    @catch_exc(test_rest_api_exception=BugCreationException)
    def __init__(self,
                 priority: str = BugPriority.LOW,
                 message: str = "",
                 expected_result: str = "",
                 actual_result: str = "",
                 steps_to_reproduce: str = ""):
        # Default data for empty data
        self._no_data_to_display = 'No data to display'
        # Save all attributes to the instance
        self.priority = priority
        self.message = message
        self.expected_result = expected_result
        self.actual_result = actual_result
        self.steps_to_reproduce = steps_to_reproduce
        # Validate message, priority, actual_result, expected_result and steps_to_reproduce
        self._validate()
        # Convert the priority to lower case and also perform trim
        self.priority = self.priority.lower().strip()
        # Exception message
        self.exc_message = f"""
BUG
---
 {settings.logging.sub_point} Priority           {settings.logging.key_val_sep} {self.priority if self.priority else self._no_data_to_display}
 {settings.logging.sub_point} Message            {settings.logging.key_val_sep} {self.message.strip() if self.message else self._no_data_to_display}
 {settings.logging.sub_point} Expected result    {settings.logging.key_val_sep} {self.expected_result.strip() if self.expected_result else self._no_data_to_display}
 {settings.logging.sub_point} Actual result      {settings.logging.key_val_sep} {self.actual_result.strip() if self.actual_result else self._no_data_to_display}
 {settings.logging.sub_point} Steps to reproduce {settings.logging.key_val_sep} {self.steps_to_reproduce.strip() if self.steps_to_reproduce else self._no_data_to_display}
"""
        super().__init__(self.exc_message)
