manha = {"Ana", "Bruno", "Carla"}
tarde = {"Bruno", "Diego", "Carla"}

print("Nos dois turnos:", sorted(manha & tarde))
print("Só de manhã:", sorted(manha - tarde))
print("Total de pessoas:", len(manha | tarde))