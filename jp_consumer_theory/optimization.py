import sympy as sp

def utility_optimize(PA, PB, Y, alpha):
    # Definimos los símbolos
    A, B, lambda_ = sp.symbols('A B lambda')

    # Parámetros del problema y función de utilidad Cobb-Douglas
    utilidad = A**alpha * B**(1 - alpha)
    restriccion = PA * A + PB * B - Y

    # Calculamos el Lagrangiano y los Lagrangianos específicos para A y B
    lagrangiano = utilidad + lambda_ * restriccion
    lagrangiano_A = utilidad + PA * A * lambda_
    lagrangiano_B = utilidad + PB * B * lambda_

    # Derivadas de los Lagrangianos específicos para A y B
    derivada_lagrangiano_A = sp.diff(lagrangiano_A, A)
    derivada_lagrangiano_B = sp.diff(lagrangiano_B, B)

    # Cociente de las derivadas ajustado por precios
    cociente_derivadas = (derivada_lagrangiano_A / PA) / (derivada_lagrangiano_B / PB)

    # Resolvemos la relación directa A en función de B
    relacion_AB = sp.Eq(derivada_lagrangiano_A / derivada_lagrangiano_B, PA / PB)
    A_en_funcion_de_B = sp.solve(relacion_AB, A)[0]

    # Sustituimos A en la restricción presupuestaria para resolver B
    restriccion_sustituida = restriccion.subs(A, A_en_funcion_de_B).simplify()
    B_optimo = sp.solve(restriccion_sustituida, B)[0]

    # Sustitución en la restricción presupuestaria simplificada y cálculo de A óptimo
    A_optimo = A_en_funcion_de_B.subs(B, B_optimo)

    # Calculamos la utilidad del consumidor con los valores óptimos de A y B
    utilidad_consumidor = utilidad.subs({A: A_optimo, B: B_optimo})

    # Imprimimos todos los resultados
    print(f"Función de utilidad: {utilidad}")
    print(f"Precio de A {PA} Precio de B {PB}")
    print(f"Restricción presupuestaria: {restriccion}")
    print(f"Lagrangiano: {lagrangiano}")
    print(f"Lagrangiano para A: {lagrangiano_A}")
    print(f"Derivada Lagrangiano para A: {derivada_lagrangiano_A}")
    print(f"Lagrangiano para B: {lagrangiano_B}")
    print(f"Derivada Lagrangiano para B: {derivada_lagrangiano_B}")
    print(f"Cociente Derivadas A/B ajustado por precios: {cociente_derivadas}")
    print(f"Lagrangiano para restricción presupuestaria: {lambda_ * restriccion}")
    
    # Cociente de precios
    cociente_precios = PA / PB
    print(f"\nCociente de precios (PA/PB): {cociente_precios}")

    # Establecemos la relación directa basada en los coeficientes y los precios
    relacion_directa = sp.Eq(derivada_lagrangiano_A / derivada_lagrangiano_B, cociente_precios)
    print(f"\nEstablecemos la relación directa A = 2B basada en los coeficientes y los precios:")
    print(f"Relación directa (derivada A / derivada B = PA / PB): {relacion_directa}")

    # Resolvemos para A en términos de B
    A_en_funcion_de_B = sp.solve(relacion_directa, A)[0]
    print(f"\nSolución para A en términos de B (simplificado): A = {A_en_funcion_de_B}")

    # Sustituimos A en la restricción presupuestaria para resolver B
    B_optimo = sp.solve(restriccion.subs(A, A_en_funcion_de_B), B)[0]

    # Sustitución en la restricción presupuestaria simplificada y cálculo de A óptimo
    print(f"Sustitución en restricción presupuestaria: {PA * A_en_funcion_de_B + PB * B - Y} = 0")
    A_optimo = A_en_funcion_de_B.subs(B, B_optimo)
    print(f"B óptimo: {B_optimo}")
    print(f"A óptimo: {A_optimo}")
    print(f"Utilidad del consumidor: {utilidad_consumidor}")

