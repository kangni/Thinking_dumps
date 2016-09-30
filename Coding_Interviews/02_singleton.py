# coding: utf-8

'''
实现 Singleton 模式

设计一个类，我们只能生成该类的一个实例。
只能生成一个实例的类是实现了 Singleton (单例)模式的类型。

在常用的模式中，Singleton 是唯一一个能够用短短几十行代码完整实现的模式。
因此，写一个 Singleton 的类型是一个很常见的面试题。

'''

# 1、使用 __new__ 方法
class singleton(object):
    def __new__(cls, *args, **kwargs):
    # __new__()在__init__()之前被调用，用于生成实例对象
        if not hasattr(cls, '_instance'):
        # 说明该类还没有实例化
            orig = super(singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
            # 实例化该类并将实例绑到cls.instance
        return cls._instance
        # 以后每次实例化都返回第一次实例化创建的实例


class MyClass(singleton):
    a = 1


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(id(a), id(b))


    
'''
# 2、共享属性
# 创建实例时把所有实例的 __dict__ 指向同一个字典，这样它们具有相同的属性和方法
class borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj


class Example(borg):
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(id(a), id(b))

'''



'''
# 3、装饰器版本

def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MyClass():
    pass

'''



'''
＃ 4、import 方法: 作为 Python 的模块是天然的单例模式

class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

from mysingleton import my_singleton

my_singleton.foo()

'''

