iterable = ['Eu', 'Tenho', '__iter__']
#iterator = iterable.__iter__() #tem __iter__e__next__
#esse iterator de baixo e uma forma mais simples de chamar o iter
iterator = iter(iterable)
for i in iterable():
    print(next(i))
