#condicional if
calificacion = input("La calificacion de la AZ900")
calificaicon = int (calificacion)
#el identado es muy importante
if calificacion < 700 :
    print("no paso")#si es menor a 700 muestra esto
elif calificacion > 1000 :
    print("miente no puedes tener esa calificacion")
else :
    print("paso")#si es mayor a 700 muestra esto

edad = input("ingrese su edad")
edad =int (edad)
if edad >= 18 and edad <=100 :
    print("bienvenid@ al mamitas")
elif edad> 100: 
    print("si vienes acompañado de tus abuelitos te podemos fiar")
elif edad < 0 :
    print("ni que fueras viajero del tiempo")
else : 
    print("no puedes llevarte esos cigarros")
    