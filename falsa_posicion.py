#------------------------------------------------------------------------------------------------- 
                            #INSTITUTO POLITÉCNICO NACIONAL

    #UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERÍA Y CIENCIAS SOCIALES Y ADMINISTRATIVAS
            
                                #INGENIERÍA EN INFORMÁTICA
                                
            #ALUMNO: GARCÍA HERNÁNDEZ ZAID ARATH
            #BOLETA: 2022602229
            #SECUENCIA: 5NV51
            #MATERIA: MÉTODOS NUMÉRICOS
#--------------------------------------------------------------------------------------------------
#LIBRERIAS
import math

#FUNCIÓN
def funcion1(x):
    if x <= 0:
        return float('inf')  # Si x es menor o igual a cero, retornar infinito positivo
    return x**2 - 4*x + 4 - math.log(x)

#INTERVALO OUTPUT
def solicitar_intervalo():
    while True:
        try:
            a = float(input("Ingrese el valor de a: "))
            if abs(a) > 1e50:
                raise ValueError("Los valores extremadamente grandes no son permitidos.")
            
            b = float(input("Ingrese el valor de b: "))
            if abs(b) > 1e50:
                raise ValueError("Los valores extremadamente grandes no son permitidos.")
            
            return a, b
        except ValueError as e:
            print(e)

#MÉTODO FALSA POSICIÓN
def falsa_posicion(funcion, a, b, tolerancia=0.0, max_iter=1000):
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con la condición de cambio de signo en el intervalo dado.")
        return None
    
    iteracion = 0
    while iteracion < max_iter:
        funcion_a = funcion(a)
        funcion_b = funcion(b)
        if funcion_a == funcion_b:
            print("La función es constante en el intervalo dado.")
            return None
        
        c = (a * funcion_b - b * funcion_a) / (funcion_b - funcion_a)
        
        error = abs(funcion(c))
        print(f"Iteración {iteracion + 1}: Raíz aproximada = {c:.20f}, Error = {error:.15f}")
        
        if error < tolerancia:
            print("La ejecución se detuvo ya que el error es menor que la tolerancia asignada.")
            return c
        
        if funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
            
        iteracion += 1
    
    print("El método de la Falsa Posición no converge dentro del número máximo de iteraciones.")
    return None

#OUTPUT
print("Se utilizará la función f(x) = x^2 - 4*x + 4 - log(x)")

#SOLICITAR INTERVALO
while True:
    try:
        a, b = solicitar_intervalo()
        break
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

print("\nUtilizando el método de la Falsa Posición:")
raiz_falsa_posicion = falsa_posicion(funcion1, a, b, tolerancia=0.0, max_iter=1000)

