from numpy import array

FechaInicio = array([22, 21, 20, 21, 21, 21, 22, 23, 24, 23, 23, 23])
SignosZodiacales = array(["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"])

def Zodiaco(day, month):
    temp = month - 1
    if(FechaInicio[month] < day):
        temp = temp + 1
    return SignosZodiacales[temp]


day = int(input("Digame su dia: "))
month = int(input("Digame su mes: "))
result = Zodiaco(day, month)
print(result)