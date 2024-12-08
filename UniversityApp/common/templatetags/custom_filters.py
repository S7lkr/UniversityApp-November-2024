from django import template
from django.contrib.auth import get_user_model

register = template.Library()


@register.filter(name='key')
def key(dict_, key_):
    """
    Custom filter which takes 2 args: "dict" and "key".
    Checks if first arg is NOT a dict: raises ValueError
    """
    if dict_.__class__ != dict:
        raise ValueError('Error: The first given argument "dict_" must be of class "dict"!')
    try:
        if type(key_) is str:
            return dict_[key_]
        elif type(key_) is int:
            return dict_.key_
    except KeyError as err:
        print(err)


@register.filter(name='index')
def index(iterable, index_: int):
    if iterable.__class__.__name__ not in ['list', 'tuple', 'QuerySet']:
        raise ValueError('The given argument "iterable" must be of class "list" or "tuple"!')
    try:
        return iterable[index_ - 1]
    except IndexError as err:
        print(err)


@register.filter(name='as_list')
def str_to_list(value: str):
    if type(value) is not str:
        raise ValueError('The given argument must be of type String!')
    try:
        return [v.strip() for v in filter(lambda x: x != "", eval(value))]
    except TypeError as err:
        print(err)


@register.filter(name='allowed_to')
def allowed_to(user, action: str):
    # if user.__class__ != get_user_model().__class__:
    #     raise TypeError('Given argument "user" must be of class "CustomUser"!')
    return action in user.get_group_permissions() or user.has_perm(action)
