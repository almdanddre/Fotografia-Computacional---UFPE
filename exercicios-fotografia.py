import math


def calcular_distancia_objeto(distancia_focal, afov, altura_objeto):
    # Convertendo o AFOV de graus para radianos
    afov_rad = math.radians(afov)
    
    # Calculando a distância do objeto usando a fórmula
    distancia_objeto = altura_objeto / (2 * math.tan(afov_rad / 2))
    
    return distancia_objeto

# Dados fornecidos
distancia_focal = 200  # Distância focal em milímetros
afov = 5  # AFOV em graus
altura_objeto = 1.8  # Altura do objeto em metros

# Calculando a distância do objeto
distancia_calculada = calcular_distancia_objeto(distancia_focal, afov, altura_objeto)

print(f'A distância do objeto em relação à luneta é: {distancia_calculada:.2f} metros')


def calcular_afov(sensor_dimensao, distancia_focal):
    # Usando a dimensão maior do sensor (assumindo um sensor retangular)
    d = max(sensor_dimensao)
    
    # Calculando o AFOV usando a fórmula
    afov_rad = 2 * math.atan(d / (2 * distancia_focal))
    
    # Convertendo o AFOV de radianos para graus
    afov_deg = math.degrees(afov_rad)
    
    return afov_deg

# Dados fornecidos
sensor_dimensao = (36, 24)  # Dimensões do sensor em milímetros (assumindo um sensor retangular)
distancia_focal = 30  # Distância focal da lente em milímetros

# Calculando o AFOV
afov_calculado = calcular_afov(sensor_dimensao, distancia_focal)

print(f'O AFOV da câmera é aproximadamente: {afov_calculado:.2f} graus')
