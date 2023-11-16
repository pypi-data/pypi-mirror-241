# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 16:02:16
# @Author  : Pane Li
# @File    : in_expect.py
"""
in_expect

"""
import typing


class expect:
    def __init__(self, value, args=None, kwargs=None):
        self._value = value
        self._args = args
        self._kwargs = kwargs

    @staticmethod
    def __dict_flatten(in_dict, separator=":", dict_out=None, parent_key=None) -> dict:
        """ 平铺字典

        :param in_dict: 输入的字典
        :param separator: 连接符号
        :param dict_out:
        :param parent_key:
        :return: dict
        """
        if dict_out is None:
            dict_out = {}

        for k, v in in_dict.items():
            k = f"{parent_key}{separator}{k}" if parent_key else k
            if isinstance(v, dict) and v:
                expect.__dict_flatten(in_dict=v, dict_out=dict_out, parent_key=k)
                continue

            dict_out[k] = v

        return dict_out

    @staticmethod
    def __dict_to_list(in_dict, list_out=None) -> list:
        """  将字典里面的所有key 和 value 转换成列表

        :param in_dict: 输入的字典
        :param list_out:

        :return: list
        """
        if list_out is None:
            list_out = []
        if in_dict is not None:
            for k, v in in_dict.items():
                list_out.append(k)
                if isinstance(v, dict):
                    expect.__dict_to_list(in_dict=v, list_out=list_out)
                    continue
                list_out.append(v)

        return list_out

    @staticmethod
    def __dict_in(expect_dict: dict, contain: dict) -> None:
        """验证字典包含关系

        :param expect_dict: dict {key: value}
        :param contain: dict,  支持${value} 表达式判断
        :return: AssertionError
        """
        if expect_dict and contain:
            contain_flatten = expect.__dict_flatten(contain)  # 平铺字典
            expect_dict_flatten = expect.__dict_flatten(expect_dict)  # 平铺字典
            for contain_item, contain_value in contain_flatten.items():
                if contain_item in expect_dict_flatten.keys():
                    value = expect_dict_flatten.get(contain_item)
                    assert value == contain_value, f'expect {expect_dict} to contain "{contain_item}":"{contain_value}"'
                else:
                    # 找出与后面相匹配的key
                    reg_item = [expect_item for expect_item in expect_dict_flatten.keys() if
                                expect_item.endswith(contain_item)]
                    if reg_item:
                        for item in reg_item:
                            value = expect_dict_flatten.get(item)
                            if value == contain_value:
                                break
                        else:
                            raise AssertionError(f'expect {expect_dict} to contain "{contain_item}":"{contain_value}"')
                    else:
                        raise AssertionError(f'expect {expect_dict} to contain keys {contain_item} ')

    @staticmethod
    def __dict_not_in(expect_dict: dict, contain: dict) -> None:
        """验证字典包含关系

        :param expect_dict: dict {key: value}
        :param contain: dict,  支持${value} 表达式判断
        :return: AssertionError
        """
        if expect_dict and contain:
            contain_flatten = expect.__dict_flatten(contain)  # 平铺字典
            expect_dict_flatten = expect.__dict_flatten(expect_dict)  # 平铺字典
            for contain_item, contain_value in contain_flatten.items():
                if contain_item in expect_dict_flatten.keys():
                    value = expect_dict_flatten.get(contain_item)
                    assert value != contain_value, f'expect {expect_dict} not contain "{contain_item}":"{contain_value}"'
                else:
                    # 找出与后面相匹配的key
                    reg_item = [expect_item for expect_item in expect_dict_flatten.keys() if
                                expect_item.endswith(contain_item)]
                    if reg_item:
                        for item in reg_item:
                            value = expect_dict_flatten.get(item)
                            if value == contain_value:
                                raise AssertionError(
                                    f'expect {expect_dict} not contain "{contain_item}":"{contain_value}"')

    def to_eq(self, expect_value):
        """Value is equal， 非严格相同， 只要值相等即可，可以是列表也可以是元组和字典等类型
           ex: expect(1).to_eq(1).to_ne(2)
           a = [1, 2, 3]
           expect(a).to_eq([1, 2, 3])
           a = {"a": 1, "b": 2}
           expect(a).to_eq({"a": 1, "b": 2})
        """
        try:
            assert self._value == expect_value, f'expect {self._value} to be {expect_value}'
        except TypeError:
            raise
        return self

    def to_ne(self, expect_value):
        """Value is not equal
           ex: expect(1).to_ne(2).to_eq(1)
        """
        try:
            assert self._value != expect_value, f'expect {self._value} not to be {expect_value}'
        except TypeError:
            raise
        return self

    def to_lt(self, expect_value):
        """Value is less than
           ex: expect(1).to_lt(2).to_gt(0)
        """
        try:
            assert self._value < expect_value, f'expect {self._value} to less than {expect_value}'
        except TypeError:
            raise
        return self

    def to_gt(self, expect_value):
        """Value is more than
           ex: expect(2).to_gt(1).to_lt(3)
        """
        try:
            assert self._value > expect_value, f'expect {self._value} to more than {expect_value}'
        except TypeError:
            raise
        return self

    def to_le(self, expect_value):
        """Value is less than or equal
           ex: expect(1).to_le(1).to_ge(1)
        """
        try:
            assert self._value <= expect_value, f'expect {self._value} to less than or equal {expect_value}'
        except TypeError:
            raise
        return self

    def to_ge(self, expect_value):
        """Value is more than or equal
           ex: expect(1).to_ge(1).to_le(1)
        """
        try:
            assert self._value >= expect_value, f'expect {self._value} to more than or equal {expect_value}'
        except TypeError:
            raise
        return self

    def to_be(self, expect_value):
        """Value is the same, 严格相同
           ex: expect(1).to_be(1).to_not_be(2), expect('1').to_be('1').to_not_be('2')
        """
        try:
            assert self._value is expect_value, f'expect {self._value} to be {expect_value}'
        except TypeError:
            raise
        return self

    def to_be_false(self):
        """Value is False  False|0|''|[]|{}|None|()"""
        try:
            assert not self._value, f'expect {self._value} to be False'
        except TypeError:
            raise
        return self

    def to_be_true(self):
        """Value is True  True|1|'1'|[1]|{"a": 1}|(1, )"""
        try:
            assert self._value, f'expect {self._value} to be True'
        except TypeError:
            raise
        return self

    def to_not_be(self, expect_value):
        """Value is not the same
           ex: expect(1).to_not_be(2).to_be(1), expect('1').to_not_be('2').to_be('1')
        """
        try:
            assert self._value is not expect_value, f'expect {self._value} to be not {expect_value}'
        except TypeError:
            raise
        return self

    def to_be_empty(self):
        """Value is empty  |''|[]|{}|()"""
        try:
            assert len(self._value) == 0, f'expect {self._value} to be empty'
        except TypeError:
            raise
        return self

    def to_contain(self, expect_value):
        """Value contains
        value = 'Hello, World'
        expect(value).to_contain('Hello')
        expect(value).to_contain(re.compile(r'Hello'))
        expect(value).to_contain(['Hello', 'World', ['Hello', 'World']])
        value = b'Hello, World'
        expect(value).to_contain(b'Hello')
        expect(value).to_contain(re.compile(rb'Hello'))
        expect(value).to_contain([b'Hello', b'World'])
        value = [1, 'Hello, World', [1, 2, 3], {'a': 1, 'b': 2}, b'hello', None, True]
        expect(value).to_contain(1)
        expect(value).to_contain('Hello, World')
        expect(value).to_contain([1, 2, 3])
        expect(value).to_contain({'a': 1, 'b': 2})
        expect(value).to_contain({'a': 1})
        expect(value).to_contain(b'hello')
        expect(value).to_contain(re.compile(r'Hello'))
        expect(value).to_contain([1, {'a': 1, 'b': 2}])
        expect(value).to_contain([1, {'a': 1, 'b': 2}, {'a': 1}])
        expect(value).to_contain([1, 2])
        expect(value).to_contain([1, 2, 3])
        expect(value).to_contain([1, 2, 3, True])
        value = {"k1": '123', 'k2': {"k2-1": None, "k2-2": {"k3": 1}}, 'k4': [123]}
        expect(value).to_contain({'k2': {"k2-1": None}})
        expect(value).to_contain({'k2-2': {"k3": 1}})
        expect(value).to_contain({'k3': 1})
        expect(value).to_contain({"k1": '123'})
        expect(value).to_contain('k2-2')
        expect(value).to_contain(None)
        expect(value).to_contain([{"k1": '123'}, {"k3": 1}])
        """
        if self._value:
            if isinstance(self._value, (str, bytes)):
                if expect_value:
                    if isinstance(expect_value, typing.Pattern):
                        assert expect_value.search(self._value), f'expect {self._value} to contain {expect_value}'
                    elif isinstance(expect_value, (list, tuple, set)):
                        for expect_value_one in expect_value:
                            self.to_contain(expect_value_one)
                    else:
                        try:
                            assert expect_value in self._value, f'expect {self._value} to contain {expect_value}'
                        except TypeError:
                            raise AssertionError(f'expect {self._value} to contain {expect_value}')
                else:
                    raise ValueError(f'expect_value is False')
            elif isinstance(self._value, (list, tuple, set)):
                if expect_value in self._value:
                    pass
                else:
                    if isinstance(expect_value, (str, typing.Pattern, bytes)):
                        if expect_value:
                            for value_one in self._value:
                                if isinstance(value_one, (str, bytes)) and expect_value.search(value_one):
                                    break
                            else:
                                raise AssertionError(f'expect {self._value} to contain {expect_value}')
                        else:
                            try:
                                assert expect_value in self._value, f'expect {self._value} to contain {expect_value}'
                            except TypeError:
                                raise AssertionError(f'expect {self._value} to contain {expect_value}')
                    elif isinstance(expect_value, (list, tuple, set)):
                        for expect_value_one in expect_value:
                            self.to_contain(expect_value_one)
                    elif isinstance(expect_value, dict):
                        if expect_value:
                            for value_one in self._value:
                                try:
                                    expect.__dict_in(value_one, expect_value)
                                    break
                                except Exception:
                                    continue
                            else:
                                raise AssertionError(f'expect {self._value} to contain {expect_value}')
                        else:
                            raise ValueError(f'expect_value is False')
                    else:
                        if expect_value:
                            for value_one in self._value:
                                try:
                                    if expect_value in value_one:
                                        break
                                except Exception:
                                    continue
                            else:
                                raise AssertionError(f'expect {self._value} to contain {expect_value}')
                        else:
                            assert expect_value in self._value, f'expect {self._value} to contain {expect_value}'
            elif isinstance(self._value, dict):
                if isinstance(expect_value, dict):
                    expect.__dict_in(self._value, expect_value)
                elif isinstance(expect_value, (list, tuple, set)):
                    for expect_value_one in expect_value:
                        self.to_contain(expect_value_one)
                else:
                    assert expect_value in self.__dict_to_list(
                        self._value), f'expect {self._value} to contain {expect_value}'
            else:
                raise TypeError(f'not support value type')
        else:
            raise ValueError(f'value is False')
        return self

    def to_not_contain(self, expect_value):
        """Value not contains
        value = 'Hello, World'
        expect(value).to_not_contain('Hello1')
        expect(value).to_not_contain(re.compile(r'Hello1'))
        expect(value).to_not_contain(['Hello1', 'World1', ['Hello1', 'World1']])
        value = b'Hello, World'
        expect(value).to_not_contain(b'Hello1')
        expect(value).to_not_contain(re.compile(rb'Hello1'))
        expect(value).to_not_contain([b'Hello1', b'World1'])
        value = [1, 'Hello, World', [1, 2, 3], {'a': 1, 'b': 2}, b'hello', None, True]
        expect(value).to_not_contain(4)
        expect(value).to_not_contain({'b': 2})
        expect(value).to_not_contain([3, 2, 4])
        expect(value).to_not_contain({'a': 1, 'b': 3})
        expect(value).to_not_contain([4, {'a': 2, 'b': 2}])
        value = {"k1": '123', 'k2': {"k2-1": None, "k2-2": {"k3": 1}}, 'k4': [123]}
        expect(value).to_not_contain({'k2': {"k2-1": 1}})
        expect(value).to_not_contain({'k2-2': {"k3": 2}})
        expect(value).to_not_contain({'k3': 2})
        expect(value).to_not_contain('k2-2-1')
        expect(value).to_not_contain(123)
        expect(value).to_not_contain([{"k1": '3'}, {"k3": 1}])
        """
        if self._value:
            if isinstance(self._value, (str, bytes)):
                if expect_value:
                    if isinstance(expect_value, typing.Pattern):
                        assert not expect_value.search(self._value), f'expect {self._value} not contain {expect_value}'
                    elif isinstance(expect_value, (list, tuple, set)):
                        for expect_value_one in expect_value:
                            self.to_not_contain(expect_value_one)
                    else:
                        try:
                            assert expect_value not in self._value, f'expect {self._value} not contain {expect_value}'
                        except TypeError:
                            pass
                else:
                    raise ValueError(f'expect_value is False')
            elif isinstance(self._value, (list, tuple, set)):
                try:
                    if expect_value in self._value:
                        raise AssertionError(f'expect {self._value} not contain {expect_value}')
                except TypeError:
                    pass
                if isinstance(expect_value, (list, tuple, set)):
                    for expect_value_one in expect_value:
                        self.to_not_contain(expect_value_one)
            elif isinstance(self._value, dict):
                if isinstance(expect_value, dict):
                    expect.__dict_not_in(self._value, expect_value)
                elif isinstance(expect_value, (list, tuple, set)):
                    for expect_value_one in expect_value:
                        self.to_not_contain(expect_value_one)
                else:
                    try:
                        assert expect_value not in self.__dict_to_list(
                            self._value), f'expect {self._value} not contain {expect_value}'
                    except TypeError:
                        pass
            else:
                raise TypeError(f'not support value type')
        else:
            raise ValueError(f'value is False')
        return self

    def to_have_length(self, expect_value):
        """Array or string has length
           ex: expect('Hello, World').toHaveLength(12)
           expect([1, 2, 3]).toHaveLength(3)
        """
        try:
            assert len(self._value) == expect_value, f'expect {self._value} to have length {expect_value}'
        except TypeError:
            raise
        return self

    def to_have_property(self, expect_key: str, expect_value: typing.Any = None):
        """dict has a property  or list contain dict has a property
            ex:
            value = {a: {b: [42]}, c: True}
            expect(value).to_have_property('a.b')
            expect(value).to_have_property('a.b', [42])
            expect(value).to_have_property('a.b[0]', 42)
            expect(value).to_have_property('c')
            expect(value).toHaveProperty('c', True)
            value = [{a: 1}, {a: 2}]
            expect(value).to_have_property('[0].a', 1)
        """
        try:
            keys = expect_key.split('.')
            expression = 'self._value'
            for key in keys:
                if key.startswith('['):
                    expression += f'{key}'
                else:
                    key_ = key.split('[', 1)[0]
                    try:
                        key_list = key.split('[', 1)[1]
                        expression += f'.get("{key_}")[{key_list}'
                    except IndexError:
                        expression += f'.get("{key_}")'
            now_value = eval(expression, {'self': self})
            if expect_value is None:
                assert now_value is not None, f'expect {self._value} to have property {expect_key}'
            else:
                if isinstance(now_value, bool) or isinstance(expect_value, bool):
                    assert eval(expression, {'self': self}) is expect_value, \
                        f'expect {self._value} to have property {expect_key} is {expect_value}'
                else:
                    assert eval(expression, {'self': self}) == expect_value, \
                        f'expect {self._value} to have property {expect_key} is {expect_value}'
        except TypeError:
            raise
        return self

    def to_match(self, expect_value: str or typing.Pattern):
        """string value matches a regular expression
           ex:
           expect('Hello, World').to_match(r'Hello')
           expect('Hello, World').to_match(re.compile(r'^Hello.*'))
        """
        import re
        try:
            assert re.match(expect_value, self._value), f'expect {self._value} to match {expect_value}'
        except TypeError:
            raise
        return self

    def to_be_instance_of(self, expect_value):
        """Value is instance of
            ex:
            value = [1, 2, 3]
            expect(value).to_be_instance_of(list)
        """
        try:
            assert isinstance(self._value, expect_value), f'expect {self._value} to be instance of {expect_value}'
        except TypeError:
            raise
        return self


class raises:

    def __init__(self, expected_exception, match=None):
        if not issubclass(expected_exception, BaseException):
            raise TypeError(f"expected_exception must be classes, not {expected_exception.__name__}")
        if not isinstance(match, (str, typing.Pattern, type(None))):
            raise TypeError(f"match must be str or typing.Pattern")
        self.expected_exception = expected_exception
        self.match = match

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if not issubclass(exc_type, self.expected_exception):
                return False
            if self.match is not None:
                if isinstance(self.match, str):
                    if self.match not in str(exc_value):
                        return False
                else:
                    if not self.match.search(str(exc_value)):
                        return False
            # 返回True表示异常已被处理，否则异常将继续传播
            return True
        else:
            raise Exception(f"DID NOT RAISE {self.expected_exception.__name__}")


if __name__ == '__main__':
    import re
    # value = 'Hello, World'
    # expect(value).to_contain('Hello')
    # expect(value).to_contain(re.compile(r'Hello'))
    # expect(value).to_contain(['Hello', 'World', ['Hello', 'World']])
    # value = b'Hello, World'
    # expect(value).to_contain(b'Hello')
    # expect(value).to_contain(re.compile(rb'Hello'))
    # expect(value).to_contain([b'Hello', b'World'])
    # value = [1, 'Hello, World', [1, 2, 3], {'a': 1, 'b': 2}, b'hello', None, True]
    # expect(value).to_contain(1)
    # expect(value).to_contain('Hello, World')
    # expect(value).to_contain([1, 2, 3])
    # expect(value).to_contain({'a': 1, 'b': 2})
    # expect(value).to_contain({'a': 1})
    # expect(value).to_contain(b'hello')
    # expect(value).to_contain(re.compile(r'Hello'))
    # expect(value).to_contain([1, {'a': 1, 'b': 2}])
    # expect(value).to_contain([1, {'a': 1, 'b': 2}, {'a': 1}])
    # expect(value).to_contain([1, 2])
    # expect(value).to_contain([1, 2, 3])
    # expect(value).to_contain([1, 2, 3, True])
    # value = {"k1": '123', 'k2': {"k2-1": None, "k2-2": {"k3": 1}}, 'k4': [123]}
    # expect(value).to_contain({'k2': {"k2-1": None}})
    # expect(value).to_contain({'k2-2': {"k3": 1}})
    # expect(value).to_contain({'k3': 1})
    # expect(value).to_contain({"k1": '123'})
    # expect(value).to_contain('k2-2')
    # expect(value).to_contain(None)
    # expect(value).to_contain([{"k1": '123'}, {"k3": 1}])

    value = 'Hello, World'
    expect(value).to_not_contain('Hello1')
    expect(value).to_not_contain(re.compile(r'Hello1'))
    expect(value).to_not_contain(['Hello1', 'World1', ['Hello1', 'World1']])
    value = b'Hello, World'
    expect(value).to_not_contain(b'Hello1')
    expect(value).to_not_contain(re.compile(rb'Hello1'))
    expect(value).to_not_contain([b'Hello1', b'World1'])
    value = [1, 'Hello, World', [1, 2, 3], {'a': 1, 'b': 2}, b'hello', None, True]
    expect(value).to_not_contain(4)
    expect(value).to_not_contain({'b': 2})
    expect(value).to_not_contain([3, 2, 4])
    expect(value).to_not_contain({'a': 1, 'b': 3})
    expect(value).to_not_contain([4, {'a': 2, 'b': 2}])
    value = {"k1": '123', 'k2': {"k2-1": None, "k2-2": {"k3": 1}}, 'k4': [123]}
    expect(value).to_not_contain({'k2': {"k2-1": 1}})
    expect(value).to_not_contain({'k2-2': {"k3": 2}})
    expect(value).to_not_contain({'k3': 2})
    expect(value).to_not_contain('k2-2-1')
    expect(value).to_not_contain(123)
    expect(value).to_not_contain([{"k1": '3'}, {"k3": 2}, 1234])
