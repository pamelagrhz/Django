print("IF")
a=4
b=45
if b > a:
    print('{} es mas grande que  {}'.format(b,a))
else:
    print('{} no es mas grande que  {}'.format(b,a))

#IF ELSE 
print("IF/ELSE")
name = 'Pamela'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Pamela':
    print('Hey Pamela!')
else:
    print('Hey anonymous!')

#IF ANIDADOS
print("IF ANIDADO")
volume = 57
if volume < 20:
    print("Algo silencioso")
elif 20 <= volume < 40:
    print("Buen volumen de musica")
elif 40 <= volume < 60:
    print("Perfecto, puedo oir los detalles")
elif 60 <= volume < 80:
    print("Cool para las fiestas")
elif 80 <= volume < 100:
    print("Algo ruidoso D=")
else:
    print("Me duelen las orejas! :(")

#Funciones
print("FUNCION")
def funcion():
    print("esta es mi primer funcion")
    print("otra linea en mi funcion")

funcion()
#Funcion con parametros
print("Funcion con parametros")
def param(name):
    if name=='Alex':
        print("hola {}".format(name))
    elif name=='Marco':
        print("hola Marco")
    else:
        print("hola "+ name + "!")


param('Marco')
param('Pamela')

#BUCLES
for i in range(1, 3):  
    print(i)

def girlsname(name):
        print(" hola {}".format(name))
print('Bucle FOR')
girls=['Viri','Jimena', 'Sara', 'Yess']

for name in girls:
        girlsname(name)

  
    