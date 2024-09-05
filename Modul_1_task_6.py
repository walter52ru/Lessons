my_dict = {'Vlad':2013,'Kostya':2018,'Vladimir':1985}
print('Dict:', my_dict)
print('Existing value', my_dict['Vlad'])
print('Not existing value:',my_dict.get('Oleg'))
my_dict.update({'Fedor':1999,'Pasha':2002})
print('Deleted value:',my_dict.pop('Kostya'))
print('Modified dictionary:',my_dict,'\n')

my_set ={1,2,3,'ser','boss',3,2}
print('Set:',my_set)
my_set.add('blue')
my_set.add(7)
my_set.discard(1)
print('Modified set:',my_set)
