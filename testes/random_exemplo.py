import random
random.seed(67)
dado = 0
tentativas = 0

while dado != 6:
    dado = random.randint(1, 6)
    tentativas += 1
    print(f"Tentativa: {tentativas}: {dado}")
print("Tirou 6!")