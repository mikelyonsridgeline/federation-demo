"""rl_validator Module is an extension on top of cerberus that extends their base validator"""
from cerberus import Validator


class ValidationException(Exception):
    """Specialized exception raised when a security isn't valid
        Attributes:
    """

    def __init__(self, errors):
        """Initialize the validation exception. Exception.message is assigned a concatenation of all the validation
        errors passed to the constructor
        """

        Exception.__init__(self, "".join(str(errors)))


class RLValidator(Validator):
    """custom validator that adds greater_than comparison to schema validation"""

    def _validate_greater_than(self, other_field, this_field, this_value):
        """validates whether the this_field's value is greater than other_fields value"""
        if other_field not in self.document:
            self._error(this_field, f"{other_field} is not in document")
            return False
        if this_value <= self.document[other_field]:
            self._error(this_field, f"not greater than {other_field}")
            return False
        return True
