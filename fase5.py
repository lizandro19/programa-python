# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Solución al Problema 5: Control de Horas de Equipo

def clasificar_jornada(horas_dias):
    """
    Función requerida para calcular la suma total de horas semanales
    y determinar la clasificación de la jornada laboral.
    """
    # Se calcula la suma de las horas usando la función integrada de Python
    total_horas = sum(horas_dias)
    
    # Lógica de negocio para clasificar la jornada
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion


def main():
    # Matriz con los datos de 4 recursos y sus horas de Lunes a Viernes
    # Formato de cada fila: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
    matriz_recursos = [
        ["Carlos Gómez", 8, 8, 9, 8, 8],     # Total: 41 (Sobretiempo)
        ["Ana Martínez", 8, 7, 8, 8, 8],     # Total: 39 (Horario Estándar)
        ["Luis Rodríguez", 9, 9, 9, 9, 8],    # Total: 44 (Sobretiempo)
        ["Sofía Benítez", 8, 8, 8, 6, 8]     # Total: 38 (Horario Estándar)
    ]
    
    print("==========================================================")
    print("       INFORME DE CONTROL DE HORAS SEMANALES")
    print("==========================================================")
    print(f"{'Nombre del Recurso':<20} | {'Total Horas':<12} | {'Clasificación':<15}")
    print("-" * 58)
    
    # Recorrido de la matriz para procesar y mostrar los datos
    for recurso in matriz_recursos:
        nombre = recurso[0]
        # Extraemos solo los valores numéricos correspondientes a las horas (índices del 1 al 5)
        horas_dias = recurso[1:]
        
        # Llamado al módulo/función
        total, jornada = clasificar_jornada(horas_dias)
        
        # Salida formateada de los resultados
        print(f"{nombre:<20} | {total:<12} | {jornada:<15}")
        
    print("==========================================================")

# Punto de entrada del script estructurado
if __name__ == "__main__":
    main()