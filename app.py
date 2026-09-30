""" productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 15},
    {"nombre": "Mouse", "precio": 25, "stock": 5},
    {"nombre": "Monitor", "precio": 75, "stock": 25},
]

productos_bajo_stock = []

for producto in productos:
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}")
    if producto['stock'] < 10:
        productos_bajo_stock.append(producto)

print("\nProductos con bajo stock:")
print(productos_bajo_stock);


def calcular_promedio_precio(lista):
    if not lista:
        return 0
    total_precio = sum(p['precio'] for p in lista)
    return total_precio / len(lista)


precio_promedio = calcular_promedio_precio(productos)
print(f"\nPrecio promedio de los productos: {precio_promedio:.2f}")

import csv

#lista donde guardaremos los datos provenientes del archivo CSV

productos_desde_csv = []

#uso del context manager 'with' en modo lectura ('r') y codificacion estandar
try:
    with open ('datos.csv', 'r', encoding='utf-8') as archivo_csv:
    #dictreader convierte cada fila del archivo csv en un diccionario
        lector_diccionario = csv.DictReader(archivo_csv)

        for fila in lector_diccionario:
            #casteo de tipos: los datos llegan como string, por lo que los forzamos a ser enteros
            fila['id'] = int(fila['id'])
            fila['precio'] = int(fila['precio'])
            fila['stock'] = int(fila['stock'])

            productos_desde_csv.append(fila)
except FileNotFoundError:
    print("Error: El archivo datos.csv no se encontró.")

print("\nLista de productos desde el archivo CSV:")
print(productos_desde_csv)

import csv
import json

def validar_datos(nombre_archivo):
    
    Valida un archivo JSON, verificando que el formato sea correcto
    y que los precios sean valores numéricos
       
    try:
        with open (nombre_archivo, 'r') as archivo_json:
            datos = json.load(archivo_json)

        if not isinstance(datos, list):
            raise ValueError("El archivo no contiene una lista de datos")

        for item in datos:
            if not isinstance(item.get('precio'), (int,float)):
                raise ValueError(f"El precio del producto {item.get('nombre')} no es un valor numérico")

        print ("Validación exitosa")
        return datos

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {nombre_archivo} no tiene un formato JSON válido.")
        return None
    except (ValueError, TypeError) as e:
        print(f"Error de validación: {e}")
        return None

if productos_desde_csv:
    datos_json = json.dumps(productos_desde_csv, indent=4)
    with open('salida.json', 'w') as archivo_salida:
        archivo_salida.write(datos_json)

    print("\nArchivo 'salida.json' creado con éxito.")

    print("\nValidando datos del archivo 'salida.json':")
    datos_validados = validar_datos('salida.json')

    if datos_validados:
        print("\nDatos validados:")
        print(datos_validados) """


import xml.etree.ElementTree as ET
tree = ET.parse("data/tasks_provider_c.xml")
root = tree.getroot()
for task in root.findall("task"):
    print({
        "title": task.find("title").text,
        "priority": task.find("priority").text,
        "status": task.find("status").text,
    })