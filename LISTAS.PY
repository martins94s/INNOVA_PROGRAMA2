familia=["jose luis","alejandra","rocio","lucas","horacio","marta"]
temperaturasJulio = [20,15,16,18,21,24,23,22,34,31,32,30,31,7,9,6,15,14,13,12,29,25,23,22,8,9,12,13,14,15,16,]
ciudades=["mendoza","buenos aires","rosario","la rioja","san luis","la pampa"]
FechasImportantes=[["2/7/1994, mi cumpeaños"],["3/9/1969, cumpleaños papa"],["7/3/1973, cumpleaños mama"]]

1#
familia.sort()
print(familia)

2#
temperaturasJulio.sort()
print(temperaturasJulio)

3#
temperaturasAgostoXquincena=[15,19,21,24,29,34,35,33,32,31,24,16,18,17,29]
julioYagosto=temperaturasJulio + temperaturasAgostoXquincena
print (julioYagosto)

4#
del familia[4]
del familia[1]
print(familia)

5#
del ciudades [3]
del ciudades[4]
print(ciudades)

6#
print(familia)
print(temperaturasJulio)
print(ciudades)
print(FechasImportantes)
print(temperaturasAgostoXquincena)

#--------------------------------------TUPLAS-------------------------------------------------------------

tupla1=("hola mundo",{"pug":"arrugas"},94,["tengo hambre"])
tupla2=("adios")
tupla3=()

tuplas = [tupla1, tupla2, tupla3]
print(tuplas)

#-------------------------------------DICCIONARIOS--------------------------------------------------------

familia={12345687:"jose luis",
         98765412:"alejandra",
         65432187:"rocio",
         987456987:"lucas"}
             

familia["horacio"]=151566156,
familia["marta"]=135615646

diccionario2={"jose":15151,"pedro":151511,"jazmin":1515}

print(diccionario2.keys())
print(diccionario2.values())
print(diccionario2.items())