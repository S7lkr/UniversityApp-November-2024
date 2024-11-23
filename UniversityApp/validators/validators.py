from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphabeticValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PasswordValidator:
    _MIN = 8
    _MAX = 20
    _HELP_TEXT = (
        f"Password must be between {_MIN} and {_MAX} symbols long!",
    )

    def __init__(self):
        self.message = PasswordValidator._HELP_TEXT

    @staticmethod
    def _messages(value):
        messages = {
            len(value) < PasswordValidator._MIN: f"Password too short! It must be at least {PasswordValidator._MIN} symbols.",
            PasswordValidator._MAX < len(value): f"Password too long! It must be no more than {PasswordValidator._MAX} symbols",
        }
        return messages

    def get_help_text(self):
        return self.message[0]

    def validate(self, value, user=None):
        if not 8 <= len(value) <= 20:
            raise ValidationError(self._messages(value)[True])
