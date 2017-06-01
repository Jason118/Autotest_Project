# -*- coding: utf-8 -*-
import yaml


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.age)

james = Person('James', 20)
print yaml.dump(james)  # 没加表示器之前


def person_repr(dumper, data):
    return dumper.represent_mapping(u'!person', {"name": data.name, "age": data.age})  # mapping表示器，用于dict

yaml.add_representer(Person, person_repr)  # 用add_representer方法为对象添加表示器
print yaml.dump(james)  # 加了表示器之后


def person_cons(loader, node):
    value = loader.construct_mapping(node)  # mapping构造器，用于dict
    name = value['name']
    age = value['age']
    return Person(name, age)

yaml.add_constructor(u'!person', person_cons)  # 用add_constructor方法为指定yaml标签添加构造器
lily = yaml.load('!person {name: Lily, age: 19}')
print lily
