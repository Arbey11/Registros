'''Se tiene un grupo de 10 registros, cada registro contiene el nombre, la edad, estatura, 
sexo (1=hombre, 2=mujer), deporte (1=natación, 2= fútbol, 3=ciclismo, 4 =otro deporte). 
Elabore un algoritmo que muestre:
Promedio de edad de las personas que prefieren el fútbol.
Porcentaje que representan las mujeres que prefieren el ciclismo respecto a las personas de ciclismo.
Cuantos de los que practican natación miden más de 1.80 mts.
Promedio de estatura de las personas que practican otro deporte que practiquen.'''

aedad = 0
cedad = 0
aest = 0
cest = 0
cnat = 0
cmujer = 0
aciclismo = 0

for i in range(10):

    nombre = input('\ningrese nombre: ')
    edad = int(input('ingrese edad: '))
    estatura = float(input('ingrese estatura: '))
    sexo = int(input('ingrese sexo, 1 = hombre, 2 = mujer, : '))
    deporte = int(input('ingrese deporte, 1 = natacion, 2 = futbol, 3 = ciclismo, 4 = otro deporte, : '))

    
    if deporte == 2:
        aedad = aedad + edad
        cedad +=1
        promedio_edad_futbol = aedad / cedad

    elif deporte == 4:
        aest = aest + estatura
        cest +=1
        promedio_est_otro_dep = aest / cest
    
    elif deporte == 1 and estatura >= 1.80:
        cnat += 1
    
    elif deporte == 3 and sexo == 2 :
        cmujer +=1
        aciclismo = aciclismo + 1
        porcentaje = (100 * cmujer) / aciclismo
    
    elif deporte == 3 and sexo == 2 or sexo == 1:
        aciclismo = aciclismo + 1

print('---------------------------------------------------------------------')
try:
    print('promedio edad prefieren futbol: ', promedio_edad_futbol,'años')
except NameError:
    print('promedio edad prefieren futbol: ', 0,'años')
try:
    print('promedio estatura otro deporte: ', promedio_est_otro_dep,'mtrs')
except NameError:
    print('promedio estatura otro deporte: ', 0, 'mtrs')
try:
    print('% mujeres que practican ciclismo respecto a las personas que practican ciclismo:', porcentaje,'%') 
except NameError:
    print('% mujeres que practican ciclismo respecto a las personas que practican ciclismo:', 0, '%') 

print('Cantidad de personas que nadan y miden mas de 1.80: ',cnat,'personas' )

