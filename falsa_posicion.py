def funcion1(x):
    return x**3 - 6*x**2 + 11*x - 6

def funcion2(x):
    return x**2 - 4

def solicitar_intervalo():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    return a, b

def solicitar_puntos_iniciales():
    p0 = float(input("Ingrese el valor inicial p0: "))
    p1 = float(input("Ingrese el valor inicial p1: "))
    return p0, p1

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
        print(f"Iteración {iteracion + 1}: raíz aproximada = {c:.20f}, error = {error:.15f}")
        
        if error < tolerancia:
            print("La ejecución se detuvo debido a que el error es menor que la tolerancia especificada.")
            return c
        
        if funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
            
        iteracion += 1
    
    print("El método de la Falsa Posición no converge dentro del número máximo de iteraciones.")
    return None

def interpolacion_inversa(funcion, p0, p1, tolerancia=0.0, max_iter=1000):
    iteracion = 0
    while iteracion < max_iter:
        f_p1 = funcion(p1)
        f_p0 = funcion(p0)
        if f_p1 == f_p0:
            print("División por cero. No se puede continuar.")
            return None
        
        p2 = p1 - f_p1 * (p1 - p0) / (f_p1 - f_p0 + 1e-9) # Método de la secante como aproximación inicial
        
        p1 = p2 - funcion(p2) * (p2 - p1) / (funcion(p2) - funcion(p1) + 1e-9) # Interpolación inversa
        
        error = abs(funcion(p1))
        print(f"Iteración {iteracion + 1}: raíz aproximada = {p1:.20f}, error = {error:.15f}")
        
        if error < tolerancia:
            print("La ejecución se detuvo debido a que el error es menor que la tolerancia especificada.")
            return p1
        
        iteracion += 1
    
    print("El método de interpolación inversa no converge dentro del número máximo de iteraciones.")
    return None

print("Seleccione la función que desea utilizar:")
print("1. f(x) = x^3 - 6*x^2 + 11*x - 6")
print("2. f(x) = x^2 - 4")
opcion = int(input("Ingrese el número de la función: "))

if opcion == 1:
    funcion = funcion1
elif opcion == 2:
    funcion = funcion2
else:
    print("Opción inválida.")
    exit()

a, b = solicitar_intervalo()
print("\nUtilizando el método de la Falsa Posición:")
raiz_falsa_posicion = falsa_posicion(funcion, a, b, tolerancia=0.0, max_iter=1000)

p0, p1 = solicitar_puntos_iniciales()
print("\nUtilizando el método de Interpolación Inversa:")
raiz_interpolacion_inversa = interpolacion_inversa(funcion, p0, p1, tolerancia=0.0, max_iter=1000)
