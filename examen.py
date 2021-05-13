def notafinalDAAM():
  #Definir variables y otros
  print("Ingrese sus calificaciones:")
  #Datos de entrada
  e1=int(input("Calificación de la unidad 01:"))
  e2=int(input("Calificación de la unidad 02:"))
  e3=int(input("Calificación de la unidad 03:"))
  e4=int(input("Calificación del trabajo final:"))
  #Proceso
  promediofinalDAAM=(e1*0.20+e2*0.15+e3*0.15+e4*0.50)
  #Datos de salida
  print("La nota final es:", promediofinalDAAM)
  

def bonoDocenteDAAM():
  #definir Variables
  bonoObtenidoDAAM=0.0
  #Datos de Endrada
  salarioMinimoDAAM=float(input("Ingrese el salario minimo:"))
  puntuacionObtenidaDAAM=float(input("Ingrese la puntuación que ha obtenido:"))
  #Proceso
  if puntuacionObtenidaDAAM<=100 and puntuacionObtenidaDAAM>=50:
    bonoObtenidoDAAM=salarioMinimoDAAM*0.10
  elif puntuacionObtenidaDAAM >=101 and puntuacionObtenidaDAAM<=150:
    bonoObtenidoDAAM=salarioMinimoDAAM*0.40
  elif puntuacionObtenidaDAAM>150:
    bonoObtenidoDAAM=salarioMinimoDAAM*0.70
  #Datos de salida
  print("El docente obtendra un bono de:", bonoObtenidoDAAM )


def saludDAAM():
  #definir Variables
  tipoDAAM=0
  sexoDAAM="M","F"
  #Datos de Endrada
  edadDAAM=float(input("Ingrese la edad:"))
  #Proceso
  if edadDAAM>=0 and edadDAAM<=15:
    tipoDAAM="tipo A"
  elif edadDAAM>=16 and edadDAAM<=69:
    print("M(masculino)     ;     F(femenino)")
    sexoDAAM=str(input("Ingrese el sexo:"))
    if sexoDAAM=="M":
      tipoDAAM="tipo A"
    elif sexoDAAM=="F":     
     tipoDAAM="tipo B"
    else:
      tipoDAAM="ERROR intentelo nuevamente"
  elif edadDAAM>=70 and edadDAAM<=123:
    tipoDAAM="tipo C"
  else:
    tipoDAAM="ERROR intentelo nuevamente"
  #Datos de salida
  print("se le aplica la vacuna:", tipoDAAM )


def calculadoraDAAM():
  #definir Variables
  resultadoDAAM=0.0
  sexoDAAM="+","-","*","/","^"
  #Datos de Endrada
  n1DAAM=float(input("Introduce tu primer número:"))
  n2DAAM=float(input("Introduce tu segundo número:"))
  print("""
    Dime, ¿qué quieres hacer?
    +) Suma
    -) Resta
    *) Multiplicación
    /) Dividisión
    **) Potenciación
    """)
  #Proceso
  opcionDAAM = str(input("Elige una opción: ") )     
  if opcionDAAM =="+":
    resultadoDAAM=n1DAAM+n2DAAM
  elif opcionDAAM =="-":
    resultadoDAAM=n1DAAM-n2DAAM
  elif opcionDAAM == "*":
    resultadoDAAM=n1DAAM*n2DAAM
  elif opcionDAAM== "/":
    resultadoDAAM=n1DAAM/n2DAAM
  elif opcionDAAM == "**":
    resultadoDAAM=n1DAAM**n2DAAM
  else:
    resultadoDAAM("Opción incorrecta")
  print("El resultado es:", resultadoDAAM )


def ejerciciosDAAM():
  print("""
  ejercicio1:  1
  ejercicio2:  2
  ejercicio3:  3
  ejercicio4:  4
  ejercicio5:  5
  """)
  ejercicioDAAM=int(input("ingrese el numero de ejercicio:"))
  if ejercicioDAAM==1:
    notafinalDAAM()
  elif ejercicioDAAM==2:
    bonoDocenteDAAM()
  elif ejercicioDAAM==3:
    saludDAAM()
  elif ejercicioDAAM==4:
    calculadoraDAAM()
  elif ejercicioDAAM==5:
    ejerciciosDAAM()
  else:
    print("opcion incorrecta")


#ejericio1
#notafinalDAAM()
#ejercicio2
#bonoDocenteDAAM()
#ejercicio3
#saludDAAM() 
#ejercicio4
#calculadoraDAAM()
#ejercicio5
ejerciciosDAAM()




