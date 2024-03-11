def funcion1(x):
    return x**3 - 6*x**2 + 11*x - 6

def funcion2(x):
    return x**2 - 4

def falsa_posicion(funcion, a, b, tolerancia=1e-10, max_iter=100):
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
        print(f"Iteración {iteracion + 1}: raíz aproximada = {c:.15f}, error = {error:.15f}")
        
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

def interpolacion_inversa(funcion, p0, p1, tolerancia=1e-10, max_iter=100):
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
        print(f"Iteración {iteracion + 1}: raíz aproximada = {p1:.15f}, error = {error:.15f}")
        
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

# Solicitar intervalo inicial [a, b] para el método de la Falsa Posición
a = float(input("Ingrese el valor de a para el método de la Falsa Posición: "))
b = float(input("Ingrese el valor de b para el método de la Falsa Posición: "))

# Llamar al método de la Falsa Posición
print("\nUtilizando el método de la Falsa Posición:")
raiz_falsa_posicion = falsa_posicion(funcion, a, b,tolerancia=1e-10,max_iter=10000)

# Solicitar puntos iniciales p0, p1 para el método de Interpolación Inversa
p0 = float(input("Ingrese el valor inicial p0 para el método de Interpolación Inversa: "))
p1 = float(input("Ingrese el valor inicial p1 para el método de Interpolación Inversa: "))

# Llamar al método de Interpolación Inversa
print("\nUtilizando el método de Interpolación Inversa:")
raiz_interpolacion_inversa = interpolacion_inversa(funcion, p0, p1, tolerancia=1e-10,max_iter=10000)
