#funcion
'''def my_fuction(fname, lname):
  print(fname +''+ lname)
my_fuction('Pepe', 'Perez')
my_fuction('Pepa', 'Pig')'''

#parameter-argument
# *args
#cameLCase
#PascaLCase
#snake_case



'''def my_fuction(*kids):
  print('The youngest child is: ' + kids[2])
  
my_fuction('Email', 'Tobias', 'Linus')
'''
'''def my_fuction(child3, child2, child1):
    print('The yogest child id: ' + child3)
my_fuction(child1= 'Emil', child2= 'Tobias', child3= 'Linus')'''

#default value
'''def my_fuction(country):
    print('I´m from ' + country)
my_fuction('Argentina')
my_fuction('Colombia')
my_fuction('')'''
#retun values
'''def my_fuction(x):
    return 5 * x
print(my_fuction(5))'''


#python lambda-funciones anonimas
'''x= lambda a : a + 10
print(x(5))

y= lambda a, b : a * b
print(y(5,6))'''