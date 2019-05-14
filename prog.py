from string import ascii_lowercase
import hashlib
import random
import time
tiempo1=time.time()
k = 0
con = "p4sswd"

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

alfanumericos = numeros + list(ascii_lowercase) #caracteres alfanumericos que puede tener el pass
# print(numeros)
# print(alfanumericos)
print("################################################################################################")
print("################################## BIENVENIDO A CRACKER p4sswd  ######3333######################")
print("################################################################################################")
print("Calculando...")

#####
# TENEMOS 4 BUCLES. 1 PARA CADA CARÁCTER ALFANÚMERICO
#####
for i in alfanumericos:
    for j in alfanumericos:
        for z in alfanumericos:
            for w in alfanumericos: #solo hay 4 bucles
                sol = i + j + z + w

                solstring = "".join(sol)

                solstring = solstring + con
                solstring.encode(encoding='UTF-8', errors='strict') #hay que codificar el string
                #print("Probando: " + solstring )

                ##########                             ###########
                #########     VAMOS A ENCRIPTAR        ###########
                #########                              ###########
                
                #m = hashlib.md5(solstring)
                s = hashlib.md5(str(solstring).encode('utf-8')).hexdigest()  #hasheamos
                #print("HASH: " + s )
                if (s == "2b51a4287ea2c750614f9eccfd505416"):  #comparamos hashes
                    k = "2b51a4287ea2c750614f9eccfd505416"
                    solucion = solstring

                if (k == "2b51a4287ea2c750614f9eccfd505416"):
                    break
    
print("-------------------------------------------")

print("-------------------------------------------")
tiempo2 = time.time()
###########################################
############   EXPLICACIÓN   ##############
###  Hacemos un encriptado              ###
###  por fuerza bruta                   ###
###  de todas las posibles              ###
###  contraseñas.                       ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###                                     ###
###########################################
###########################################
##########################################
print("La solución es: " + solucion)
a = tiempo2-tiempo1
print(a)
print ("Calculada en: "  + str(a) + " segundos.") 
print("Puede cambiar el patrón de la contraseña dentro del ejecutable.")
