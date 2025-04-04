nombres = [
    "Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía", "Miguel", "Elena",
    "Jorge", "Paula", "Andrés", "Valeria", "Raúl", "Gabriela", "Esteban", "Marta", "Felipe", "Camila",
    "Ricardo", "Beatriz", "Daniel", "Patricia", "Fernando", "Rosa", "Héctor", "Clara", "Alberto", "Diana",
    "Emilio", "Verónica", "Roberto", "Isabel", "Manuel", "Lucía", "Gonzalo", "Teresa", "Ramón", "Natalia",
    "Victor", "Susana", "Oscar", "Jimena", "Diego", "Alicia", "Samuel", "Lorena", "Pablo", "Julia"
]
generos = [
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
    "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"
]
edades_actuales = [
    25, 50, 34, 40, 60, 70, 45, 55, 80, 90,
    30, 48, 37, 42, 65, 75, 50, 60, 85, 95,
    28, 53, 32, 47, 58, 67, 40, 52, 76, 88,
    22, 44, 36, 41, 63, 72, 46, 57, 78, 89,
    27, 49, 31, 43, 59, 68, 39, 51, 77, 87
]
enfermedades = [
    "No", "Sí", "No", "No", "Sí", "No", "Sí", "No", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí",
    "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí", "No", "Sí"
]

def calcular_indice_riesgo(edad, genero, enfermedad):
    riesgo = 0
    if genero == "M":
        riesgo += 1
    if enfermedad == "Sí":
        riesgo += 1
    if edad > 60:
        riesgo += 1
    return riesgo

riesgos = []

def riesgo_fun(edad, genero, enfermedad, index):
    if index < len(edad):
        riesgo = calcular_indice_riesgo(edad[index], genero[index], enfermedad[index])
        riesgos.append(riesgo)
        riesgo_fun(edad, genero, enfermedad, index + 1)
    else:
        print('\n')
    
riesgo_fun(edades_actuales, generos, enfermedades, 0)
print(riesgos)

def gompertz_makeham(x, A, B, c):
    return A + B * (c ** (x / 10.0))

def error_cuadrado(observado, predicho):
    return (observado - predicho) ** 2

def ajustar_gompertz_makeham(edades, tasas_mortalidad_observadas, iteraciones=1000):
    A= 0.001
    B= 0.0001
    c= 1.1
    tasa_aprendizaje = 0.000001
    