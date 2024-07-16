immutable_var = 1, 2, True, 'd', 'a'
print(immutable_var)
#immutable_var[1] = 21
#print(immutable_var)
# такой тип кортежа не потдерживает обращение по элементам
mutable_list = ['a', 'b', 'c', 5, 4]
mutable_list[0] = 1
mutable_list.append('geam')
mutable_list.extend('time')
mutable_list.extend(['cat', 2])
mutable_list.remove('c')
print(mutable_list)