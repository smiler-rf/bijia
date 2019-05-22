# class A(object):
#     def foo(self, x):
#         print("executing foo(%s,%s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s,%s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
#
#
# a = A()
# a.foo(2)
# A.class_foo(2)
# A.static_foo(2)
#
# def print_everything(*args):
#     for count, thing in enumerate(args):
#         print('{0}.{1}'.format(count, thing))
# print_everything('apple', 'banana', 'cabbage')
#
# import copy
# a = [1,2,3,4, ['a','b']]
# b = a # 直接赋值，传递对象的引用
# c = copy.copy(a) # 浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
# d = copy.deepcopy(a) # 深拷贝，包含对象里面的子对象的拷贝，所以原始对像改变不会造成深拷贝里任何子元素改变
#
# a.append(5)
# a[4].append('c')
#
# print('a:',a)
# print('b:',b)
# print('c:',c)
# print('d:',d)
#
#
# def print_directory_content(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_content(sChildPath)
#         else:
#             print(sChildPath)
# print_directory_content("F:\重要文件")



# class Node(object):
#     def __init__(self,sName):
#         self._lChildren = []
#         self.sName = sName
#     def __repr__(self):
#         return "<Node '{}'>".format(self.sName)
#     def append(self,*args,**kwargs):
#         self._lChildren.append(*args,**kwargs)
#     def print_all_1(self):
#         print(self)
#         for oChild in self._lChildren:
#             oChild.print_all_1()
#     def print_all_2(self):
#         def gen(o):
#             lAll = [o,]
#             while lAll:
#                 oNext = lAll.pop(0)
#                 lAll.extend(oNext._lChildren)
#                 yield oNext
#         for oNode in gen(self):
#             print(oNode)
#
# oRoot = Node("root")
# oChild1 = Node("child1")
# oChild2 = Node("child2")
# oChild3 = Node("child3")
# oChild4 = Node("child4")
# oChild5 = Node("child5")
# oChild6 = Node("child6")
# oChild7 = Node("child7")
# oChild8 = Node("child8")
# oChild9 = Node("child9")
# oChild10 = Node("child10")
#
# oRoot.append(oChild1)
# oRoot.append(oChild2)
# oRoot.append(oChild3)
# oChild1.append(oChild4)
# oChild1.append(oChild5)
# oChild2.append(oChild6)
# oChild4.append(oChild7)
# oChild3.append(oChild8)
# oChild3.append(oChild9)
# oChild6.append(oChild10)
#
# oRoot.print_all_1()
# oRoot.print_all_2()

# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]
#
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]
#
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l2 if i<(0.5*0.5)]
#
# import cProfile # 分析代码性能
# import random
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')
# cProfile.run('f3(lIn)')


l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l1.index)
print(l2)
