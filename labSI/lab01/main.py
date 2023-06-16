
import re

# Realizar las siguientes sustituciones: axo, hxi, ñxm, kxl, uxv, wxv, zxy, xxr 
# (tanto mayúsculas como minúsculas). 
def sustituciones(texto):
    sustituciones_dict = {
        'a': 'o', 
        'h': 'i', 
        'ñ': 'm', 
        'k': 'l', 
        'u': 'v', 
        'w': 'v', 
        'z': 'y', 
        'x': 'r'
    }

    for k, v in sustituciones_dict.items():
        texto = re.sub(r'{}'.format(k), v, texto, flags=re.IGNORECASE)
    return texto

#Elimine las tildes
def eliminar_tildes(texto):
    tildes_dict = {
        'á': 'a', 
        'é': 'e', 
        'í': 'i', 
        'ó': 'o', 
        'ú': 'u', 
        'Á': 'A', 
        'É': 'E', 
        'Í': 'I', 
        'Ó': 'O', 
        'Ú': 'U'
    }
    for k, v in tildes_dict.items():
        texto = texto.replace(k, v)
    return texto

# Convierta todas las letras a mayúsculas
def mayusculas(texto):
    return texto.upper()

# Elimine los espacios en blanco y los signos de puntuación 

def eliminar_espacios_puntuacion(texto):
    texto = re.sub(r'[\s\W]+', '', texto)
    return texto

# Indique cuál sería el alfabeto resultante y cuál su longitud
def obtener_alfabeto(texto):
    texto = eliminar_espacios_puntuacion(texto)
    alfabeto = set(texto)
    longitud = len(alfabeto)
    return alfabeto, longitud

# implementar una función que calcule una tabla de frecuencias para cada 
# letra de la ’A’ a ’Z’. 
def frecuencias(archivo):

    frecuencias_dict = {}
    with open(archivo, 'r') as file:
        texto = file.read()
    
    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        frecuencias_dict[letra] = texto.count(letra)
    
    return frecuencias_dict

# Reconozca en el resultado obtenido los cinco caracteres de mayor frecuencia
def caracteres_mayor_frecuencia(frecuencias_dict):
    frecuencias_mayor = sorted(frecuencias_dict.items(), key=lambda x: x[1], reverse=True)[:5]
    return frecuencias_mayor

# , para ello deberá recorrer el texto preprocesado y hallar los trigramas
#  en el mismo (sucesión de tres letras seguidas que se repiten) y 
# las distancias (número de caracteres entre dos trigramas iguales consecutivos) 
def obtener_trigramas_y_distancias(texto):
    trigramas = set()
    distancias = []
    
    for i in range(len(texto)-2):
        trigrama = texto[i:i+3]
        if texto.count(trigrama) > 1:
            trigramas.add(trigrama)
            indice = texto.index(trigrama)
            distancia = texto.index(trigrama, indice+1) - indice
            distancias.append(distancia)
    
    return trigramas, distancias

# Hexadecimal
def convertir_a_hexadecimal(numero):
    digitos_hex = "0123456789ABCDEF"
    resultado = ""
    
    if numero == 0:
        return "0"
    
    while numero > 0:
        residuo = numero % 16
        resultado = digitos_hex[residuo] + resultado
        numero = numero // 16
    
    return resultado

# Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8
def preprocesar_a_unicode8(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file:
        texto = file.read()
    
    texto_unicode8 = ""
    for caracter in texto:
        texto_unicode8 += "U+" + str(convertir_a_hexadecimal(ord(caracter)).zfill(4)) + " "
    
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_unicode8)

# Volver a preprocesar el archivo insertando la cadena AQP cada 20 caracteres,
#  el texto resultante deberá contener un número de caracteres que sea múltiplo 
# de 4, si es necesario rellenar (padding) al final con caracteres X según se 
# necesite
def preprocesar_con_padding(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file:
        texto = file.read()

    texto_procesado = ""
    contador = 0
    for caracter in texto:
        if contador % 20 == 0 and contador > 0:
            texto_procesado += "AQP"
        texto_procesado += caracter
        contador += 1

    if len(texto_procesado) % 4 != 0:
        padding = 4 - (len(texto_procesado) % 4)
        texto_procesado += "X" * padding

    with open(archivo_salida, 'w') as file:
        file.write(texto_procesado)

if __name__ == '__main__':
    # Leer el archivo de texto
    with open('text.txt', 'r') as file:
        texto = file.read()
    
    # Realizar las sustituciones, eliminar tildes, convertir a mayúsculas y eliminar espacios y puntuación
    texto = sustituciones(texto)
    texto = eliminar_tildes(texto)
    texto = mayusculas(texto)
    texto = eliminar_espacios_puntuacion(texto)
    
    # Guardar el resultado en un archivo
    with open('POEMA_PRE.txt', 'w') as file:
        file.write(texto)
    
    # Obtener el alfabeto y su longitud
    alfabeto, longitud = obtener_alfabeto(texto)
    
    # Imprimir el resultado
    print(f'Texto preprocesado: {texto}')
    print(f'Alfabeto: {alfabeto}')
    print(f'Longitud del alfabeto: {longitud}')
    
    # Calcular las frecuencias de cada letra
    frecuencias_dict = frecuencias('POEMA_PRE.txt')
    
    # Imprimir las cinco letras de mayor frecuencia
    caracteres_mayor_frecuencia_dict = caracteres_mayor_frecuencia(frecuencias_dict)
    print(f'Caracteres de mayor frecuencia: {caracteres_mayor_frecuencia_dict}')
    
    # Obtener los trigramas y distancias
    with open('POEMA_PRE.txt', 'r') as file:
        poema_pre = file.read()
        trigramas, distancias = obtener_trigramas_y_distancias(poema_pre)
     
    # Imprimir los trigramas y distancias
    print(f'Trigramas encontrados: {trigramas}')
    print(f'Distancias: {distancias}')
    
    # Preprocesar a UNICODE-8
    preprocesar_a_unicode8('text.txt', 'unicode8.txt')
    
    # Preprocesar con padding
    preprocesar_con_padding('POEMA_PRE.txt', 'AQP.txt')