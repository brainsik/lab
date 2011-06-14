# encoding: utf-8
from nose.tools import raises

from attrdict import AttrDict


@raises(TypeError)
def test_item_is_invalid_identifier():
    d = AttrDict()
    d['bad-wolf'] = "rose"


@raises(TypeError)
def test_item_is_builtin_attribute():
    d = AttrDict()
    d['__class__'] = "working"


@raises(TypeError)
def test_init_item_is_builtin_attribute():
    AttrDict(get="smart")


@raises(KeyError)
def test_pop_removes_item():
    d = AttrDict(k=True)
    try:
        d['k']
    except KeyError:
        assert False, "KeyError shouldn't be raised yet"
    d.pop('k')
    d['k']


@raises(AttributeError)
def test_pop_removes_attr():
    d = AttrDict(k=True)
    try:
        d.k
    except AttributeError:
        assert False, "AttributeError shouldn't be raised yet"
    d.pop('k')
    d.k


@raises(AttributeError)
def test_delete_item_removes_attr():
    d = AttrDict(k=True)
    del d['k']
    d.k


@raises(KeyError)
def test_delete_attr_removes_item():
    d = AttrDict(k=True)
    del d.k
    d['k']


def test_copy_returns_our_type():
    d = AttrDict(k=True)
    assert d.copy().__class__ is AttrDict


def test_fromkeys_returns_our_type():
    d = AttrDict.fromkeys(['scotch', 'rye', 'bourbon'], "whiskey")
    assert d.__class__ is AttrDict
