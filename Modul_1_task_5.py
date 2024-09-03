immutable_var = (1 , True, 7.7, 'Apple')
print ('Immutable tuple:',immutable_var)

# immutable_var[0] = 7 # Нельзя изменять, так как кортеж является не изменяемым. Изменять можно только список, если внесенти его внутри кортежа.

mutable_list = [1 , True, 7.7, 'Apple']
print ('Mutable list:',mutable_list)
mutable_list[0] = False
print ('Mutable list:',mutable_list)
mutable_list.append(tuple([7,6,5]))
print ('Mutable list:',mutable_list)
mutable_list.remove('Apple')
print ('Mutable list:',mutable_list)