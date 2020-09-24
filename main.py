

FechaInicio = [22, 21, 20, 21, 21, 21, 22, 23, 24, 23, 23, 23]
SignosZodiacales = ["capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]


def Zodiaco(day, month):
    temp = month - 1
    fecha = FechaInicio[month]
    if(fecha < day):
        temp = temp + 1
    result = SignosZodiacales[temp]
    return result


day = int(input("Digame su dia: "))
month = int(input("Digame su mes: "))
result = Zodiaco(day, month)
print(result)