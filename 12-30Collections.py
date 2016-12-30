#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     30/12/2016
# Copyright:   (c) 12SigmaTech 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

## tuple
# tuple-->immutable)
empty=()
print type(empty)   # 'tuple'
one=('Canary')
two=('Cannary','a')
print type(one),type(two)  # 'str'  'tuple'

# slicing
names=['a','b','c','d','e']
print names[0],names[:4],names[-3:-1]  # a ['a', 'b', 'c', 'd'] ['c', 'd']
print type(names[0]),type(names[:4])  # 'str'  'list'
names=names[0],'f',names[1],names[3]
print type(names),names  # 'tuple' ('a','f','b','d')

# len()
pets=(('dog',2),('cat',4),('Hamster',12))
print len(pets)  # 3
print pets[2][0] # Hamster

##list
#list-->(alterable)
fruit=['apple','Hawthorn','Loquat','Medlar','Pear','Quince']
print fruit[4:4]  #  []
print fruit[:2],type(fruit[:2])  # 'apple' 'Hawthorn'  type==>list
print fruit[0],type(fruit[0])  # apple   type==>str

# insert
fruit.insert(4,'Rowan')
print fruit  #  ['apple', 'Hawthorn', 'Loquat', 'Medlar', 'Rowan', 'Pear', 'Quince']

#del
del fruit[4]
print fruit  #  ['apple', 'Hawthorn', 'Loquat', 'Medlar', 'Pear', 'Quince']

# Using slice do the same work
fruit[4:4]=['Rowan']
print fruit  #  ['apple', 'Hawthorn', 'Loquat', 'Medlar', 'Rowan', 'Pear', 'Quince']
fruit[4:5]=[]
print fruit  #  ['apple', 'Hawthorn', 'Loquat', 'Medlar', 'Pear', 'Quince']

fruit[2:3]=['Plum','Peach']
print fruit  #  ['apple', 'Hawthorn', 'Plum', 'Peach', 'Medlar', 'Pear', 'Quince']

## dict
# dict-->alterable
insects={'Dragonfly':5000,'Praying Mantis':2000,'Fly':12000,'Beetle':35000}
print insects['Fly']
print insects
insects['Grasshopper']=200000  # append
print insects

# del
del insects['Fly']
print insects

insects.pop('Beetle')
print insects
for key,value in insects.items():
    print key,'==>',insects.keys()
    print value,'==>',insects.values()


