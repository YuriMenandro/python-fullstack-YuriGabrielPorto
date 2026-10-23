import math

p1 = (3, 4)
p2 = (7, 1)
x1, y1 = p1
x2, y2 = p2
dif_quadrado_x = (x2 - x1) ** 2
dif_quadrado_y = (y2 - y1) ** 2

distancia = math.sqrt(dif_quadrado_x + dif_quadrado_y)
print(f"Distância entre os pontos: {distancia:.4f}")