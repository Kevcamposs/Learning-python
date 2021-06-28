# Objetivo: Crear programa que convierta grados, minutos y segundos a grados decimanles

Grades = int(input("Ingrese los grados: "))
Minutes = int(input("Ingrese los minutos: "))
Seconds = float(input("Ingrese los segundos: "))

Expression = Grades + (Minutes*1/60 + Seconds*1/60) # Conversión
Expression = round(Expression, 4) # Considerar 4 decimales
print("En grados decimales es: ", str(Expression) + "°")