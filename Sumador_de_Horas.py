hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos) "))
# encuentra el número total de minutos
totalMins = mins + dura
print("Total Minutos",totalMins)
# encuentra el número de horas ocultas en los minutos y actualiza las horas
totalHour = totalMins // 60
print("Total Horas", totalHour)
# corrige los minutos para que estén en un rango de (0..59)
mins = totalMins % 60

# corrige las horas para que estén en un rango de (0..23) 
hour+=totalHour
hour%=24
print(hour, ":", mins, sep='')