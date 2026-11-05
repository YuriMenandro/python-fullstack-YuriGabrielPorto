metros = float(input("Digite uma distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegada = metros * 39.37
pes = metros * 3.281



print(f"{"="*26}")
print(f"{"Unidade":<12}{"Valor":>14}")
print(f"{"="*26}")
print(f"{"km:":<12}{km:>14.2f}")
print(f"{"cm:":<12}{cm:>14.2f}")
print(f"{"mm:":<12}{mm:>14.2f}")
print(f"{"polegadas:":<12}{polegada:>14.2f}")
print(f"{"pés:":<12}{pes:>14.2f}")
print(f"{"="*26}")