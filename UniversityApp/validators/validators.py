from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PasswordLengthValidator:
    _MIN = 8
    _MAX = 40
    _HELP_TEXT = f"Password must be between {_MIN} and {_MAX} symbols long!"

    def __init__(self):
        self.help_text = PasswordLengthValidator._HELP_TEXT

    @staticmethod
    def _error_messages(value):
        error_messages = {
            len(value) < PasswordLengthValidator._MIN: f"Password too short! It must be at least "
                                                       f"{PasswordLengthValidator._MIN} symbols.",
            PasswordLengthValidator._MAX < len(value): f"Password too long! It must be no more than "
                                                       f"{PasswordLengthValidator._MAX} symbols",
        }
        return error_messages

    def get_help_text(self):
        return self.help_text

    def validate(self, value, user=None):
        if not 8 <= len(value) <= 20:
            raise ValidationError(self._error_messages(value)[True])

    def __call__(self, value):
        pass


@deconstructible
class AlphabeticValidator:
    def __init__(self, err_message=None):
        self.err_message = err_message

    @property
    def err_message(self):
        return self.__err_message

    @err_message.setter
    def err_message(self, value):
        if value is None:
            self.__err_message = "No symbols allowed in name!"
        else:
            self.__err_message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.err_message)


@deconstructible
class CapitalizedValidator:
    def __init__(self, err_message=None):
        self.err_message = err_message

    @property
    def err_message(self):
        return self.__err_message

    @err_message.setter
    def err_message(self, value):
        if value is None:
            self.__err_message = "Name must be capitalized!"
        else:
            self.__err_message = value

    def __call__(self, value):
        if not value[0].isupper():
            raise ValidationError(self.err_message)
