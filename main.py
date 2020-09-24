FechaInicio = [22, 21, 20, 21, 21, 21, 22, 23, 24, 23, 23, 23]
SignosZodiacales = ["capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]


def Zodiaco(day, month):
    temp = month - 1            #  resta 1 para igualar al array 
    fecha = FechaInicio[temp]   #  mes es lo mismo que posicion en array 
    if(fecha <= day):            #  el dia que corresponde es menor se pone el signo actual si es mayor se pasa al sig.
        temp = temp + 1         #  pasa al siguiente signo 
    if(temp >= 12):
        temp = month - 11

    result = SignosZodiacales[temp]     # asignar el resultado 
    return result


day = int(input("Digame su dia: "))
month = int(input("Digame su mes: "))
result = Zodiaco(day, month)
print(result)