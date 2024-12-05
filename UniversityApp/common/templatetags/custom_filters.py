from django import template

register = template.Library()


@register.filter(name='key')
def key(dict_, key_):
    if dict_.__class__ == dict:
        if type(key_) is str:
            return dict_[key_]
        elif type(key_) is int:
            return dict_.key_
    raise ValueError('The given argument "dict_" must be of class "dict"!')


@register.filter(name='index')
def index(iterable, index_: int):
    if iterable.__class__ in [list, set, tuple]:
        return iterable[index_ - 1]
    raise ValueError('The given argument "iterable" must be of class "list/set/tuple"!')
