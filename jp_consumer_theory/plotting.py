import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def optimum_plot(PA, PB, Y, alpha):
    # Definir la restricción presupuestaria
    A = np.linspace(0.01, Y/PA, 500)  # Asegurar que A no empiece en 0 para evitar divisiones por cero
    B = (Y - PA * A) / PB  # B según la restricción presupuestaria

    # Función para resolver el punto óptimo
    def equations(vars):
        A, B = vars
        eq1 = PA * A + PB * B - Y
        eq2 = (alpha / A) - ((1 - alpha) / B) * (PB / PA)
        return [eq1, eq2]

    # Solución inicial aproximada
    A_guess = Y / (2 * PA)
    B_guess = Y / (2 * PB)

    # Resolver el sistema de ecuaciones para encontrar las cantidades óptimas
    optimal_A, optimal_B = fsolve(equations, (A_guess, B_guess))

    # Calcular la utilidad en el punto óptimo
    optimal_U = optimal_A**alpha * optimal_B**(1 - alpha)

    # Graficar la restricción presupuestaria
    plt.figure(figsize=(8, 6))
    plt.plot(A, B, label='Restricción Presupuestaria')  # Restricción presupuestaria

    # Curvas de indiferencia cerca del punto óptimo
    U_optimal = optimal_U
    U_vals_optimal = [U_optimal * 0.8, U_optimal * 1.2]  # Ajuste en el rango de utilidades para mejor visualización

    for U in U_vals_optimal:
        B_indif = np.maximum((U / (A**alpha))**(1/(1-alpha)), 0)  # Asegurar que B_indif sea positivo
        plt.plot(A, B_indif, linestyle='--', linewidth=1)

    # Resaltar el punto óptimo
    plt.scatter(optimal_A, optimal_B, color='red', zorder=5, label='Punto Óptimo')

    # Añadir anotación para el punto óptimo y la utilidad
    plt.annotate(f'(A={optimal_A:.2f}, B={optimal_B:.2f}) ; Utilidad={optimal_U:.2f}', 
                 (optimal_A, optimal_B), textcoords="offset points", xytext=(10,-10),
                 ha='center', color='blue')

    # Ajustes finales al gráfico basados en los valores óptimos
    plt.xlim(0, max(A.max(), optimal_A) * 1.1)
    plt.ylim(0, max(B.max(), optimal_B) * 1.1)
    plt.xlabel('Cantidad de A')
    plt.ylabel('Cantidad de B')
    plt.title('Solución Óptima con Función de Utilidad Cobb-Douglas')
    plt.legend()
    plt.grid(True)
    plt.show()


