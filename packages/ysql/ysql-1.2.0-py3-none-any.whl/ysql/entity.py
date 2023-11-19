# -*- coding: utf-8 -*-

from typing import Union


def Entity(check_type=False):
    """更改返回的值，如果不使用此装饰器，则始终完整返回默认值（包括约束），这在单独使用数据类的时候很不便，但对于建表（需要知道约束）和插入（需要知道主键约束）不影响
    仅在单独使用数据类的时候有效"""

    def decorator(cls):
        orig_getattribute = cls.__getattribute__
        orig_init = cls.__init__

        def new_getattribute(self, name):
            # 该类的属性名集合
            attr_names = set(attr_name for attr_name, attr_type in cls.__annotations__.items())
            # 只有访问属性时才进一步处理
            if name in attr_names:
                value = orig_getattribute(self, name)
                return parse_default_value(value)
            # 否则返回原始值
            return orig_getattribute(self, name)

        def init_and_check_type(self, *args, **kwargs):
            orig_init(self, *args, **kwargs)

            for attr_name, attr_type in cls.__annotations__.items():
                # 首先检查类型注解自身是否满足要求
                if attr_type not in {int, str, float, bytes}:
                    raise TypeError(
                        f"定义'{cls.__name__}'类时，"
                        f"'{attr_name}'属性的类型应该属于: 'int'、'str'、'float'、'bytes'，"
                        f"但得到的是'{attr_type.__name__}'")

                # 再检查属性类型与类型注解是否一致
                attr_value = new_getattribute(self, attr_name)
                if not isinstance(attr_value, attr_type):
                    raise TypeError(
                        f"实例化'{cls.__name__}'类时,"
                        f"'{attr_name}'属性的类型应该是'{attr_type.__name__}',"
                        f"但得到的是'{type(attr_value).__name__}'")

        # 由于无参装饰器的特性，在无参使用该装饰器时，check_type的值被覆盖为cls，因此必须显式的与True进行判断
        if check_type == True:  # noqa
            cls.__init__ = init_and_check_type
        cls.__getattribute__ = new_getattribute
        return cls

    # 无参使用该装饰器时
    if callable(check_type):
        return decorator(cls=check_type)

    return decorator


class Constant:
    """存储特殊形式的常量"""
    PRIMARY_KEY = ("PRIMARY KEY",)
    AUTO_PRIMARY_KEY = ("PRIMARY KEY AUTOINCREMENT",)
    NOT_NULL = ("NOT NULL",)
    UNIQUE = ("UNIQUE",)

    NO_ACTION = 'NO ACTION'
    RESTRICT = 'RESTRICT'
    CASCADE = 'CASCADE'
    SET_NULL = 'SET NULL'
    SET_DEFAULT = 'SET DEFAULT'


class Constraint:
    """提供对字段的各种约束"""

    # =================================================================================================================
    # 1.可直接使用的约束常量
    primary_key = Constant.PRIMARY_KEY  # 主键
    auto_primary_key = Constant.AUTO_PRIMARY_KEY  # 自增主键
    not_null = Constant.NOT_NULL  # 非空
    unique = Constant.UNIQUE  # 唯一

    # 针对外键的约束
    no_action = Constant.NO_ACTION
    cascade = Constant.CASCADE
    set_null = Constant.SET_NULL
    restrict = Constant.RESTRICT
    set_default = Constant.SET_DEFAULT

    # =================================================================================================================
    # 2.需要外部传值的约束
    @staticmethod
    def default(default_value: Union[int, str, float, bytes]):
        """默认值约束"""
        if type(default_value) in {int, str, float, bytes}:
            return (f'DEFAULT {default_value}',)  # noqa
        raise TypeError(f'数据类型不匹配，允许的数据类型为: int, str, float, bytes')

    @staticmethod
    def check(check_condition: str):
        """条件约束"""
        if type(check_condition) in {str}:
            return (f'CHECK({check_condition})',)  # noqa
        raise TypeError(f'数据类型不匹配，允许的数据类型为: str')

    @staticmethod
    def foreign_key(entity, field, delete_link=None, update_link=None):
        """外键约束"""
        return ((entity.__name__, field, delete_link, update_link),)  # noqa

    @staticmethod
    def comment(comment: str):
        """字段注释"""
        if type(comment) in {str}:
            return (f'-- {comment}\n',)  # noqa
        raise TypeError(f'数据类型不匹配，允许的数据类型为: str')


def parse_constraints(attr_value):
    """从原始属性值中解析出约束条件"""
    if not isinstance(attr_value, tuple):
        return []

    # 单元素元组
    if len(attr_value) == 1:
        return list(attr_value)

    # 多元素元组
    elif len(attr_value) > 1:
        constraints = []

        for item in attr_value:
            if not isinstance(item, tuple):
                continue
            # 元素也是元组，说明是约束条件
            if len(item) == 1:
                constraints.append(item[0])
            else:
                raise TypeError(f'约束条件必须为长度为1的元组，错误的数据: {item}')

        return constraints

    else:
        raise TypeError(f'属性值的数据结构不满足要求，无法解析出sql约束\n传入的值: {attr_value}')


def parse_default_value(attr_value):
    """从原始属性值中解析出是基本类型的唯一属性默认值"""
    # 属性值就是基本类型
    if isinstance(attr_value, (int, str, float, bytes)) or attr_value is None:
        return attr_value

    # 检查是否为元组
    if not isinstance(attr_value, tuple):
        raise TypeError('该属性值的类型不满足要求，只允许基本类型和元组')

    # 用列表保存匹配到的基本属性值，用来进一步检验该值是否唯一
    value_list = [value for value in attr_value
                  if isinstance(value, (int, str, float, bytes))]

    list_length = len(value_list)
    # 没有默认值
    if list_length == 0:
        return None
    # 有唯一的默认值
    elif list_length == 1:
        return value_list[0]
    else:
        raise TypeError('错误传递了多个基本数据类型的默认值，只允许有一个默认值')
