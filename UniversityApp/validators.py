from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersOnlyValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PasswordValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Password must must contain only letters, digits and underscores!"
        else:
            self.__message = value

    def __call__(self, value):
        if not all(ch.isalnum() or ch == '_' for ch in value):
            raise ValidationError(self.message)
